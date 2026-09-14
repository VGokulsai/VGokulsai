"""Write the numbers on the profile from live data, so nobody types them.

A number a human types is a number that can be wrong, and this one already was:
the profile said thirteen public repos when there were twelve, on a page whose
whole claim is that its figures are checkable.

    py -3 stats.py            rewrite the block in README.md
    py -3 stats.py --check    print what it would write, change nothing

If GitHub cannot be reached, this refuses to write anything. Replacing a real
number with a zero because the network was down is the same bug as a search
that reports "nobody has this problem" when it was rate limited.
"""

import argparse
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request

USER = "VGokulsai"
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
START, END = "<!-- stats:start -->", "<!-- stats:end -->"

# Spelled out up to twenty, because the sentence around it is prose.
WORDS = ("zero one two three four five six seven eight nine ten eleven twelve "
         "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
         ).split()


class Blocked(Exception):
    """Could not read GitHub. Not the same as having nothing to report."""


def repos():
    """Every public repo the user owns, forks excluded."""
    out, page = [], 1
    while page < 10:
        url = ("https://api.github.com/users/%s/repos?per_page=100&page=%d"
               % (USER, page))
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "%s-profile-stats" % USER,
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status != 200:
                    raise Blocked("GitHub answered %s" % r.status)
                rows = json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raise Blocked("GitHub answered %s %s" % (exc.code, exc.reason))
        except Exception as exc:
            raise Blocked("could not reach GitHub: %s" % exc)
        if not rows:
            break
        out.extend(rows)
        if len(rows) < 100:
            break
        page += 1
    if not out:
        # An account with no repositories is possible; an empty answer from an
        # API that just returned 200 is much more likely to be a wrong URL.
        raise Blocked("GitHub returned no repositories at all for %s" % USER)
    return [r for r in out if not r.get("fork")]


def count(n):
    return WORDS[n] if n < len(WORDS) else str(n)


def sentence(own):
    # The profile repo is one of the twelve but it is not a project, so it is
    # counted and named rather than quietly dropped.
    projects = [r for r in own if r["name"].lower() != USER.lower()]
    return ("%s public repos, all written on my own, of which %s are projects "
            "and one is this profile." % (count(len(own)).capitalize(),
                                          count(len(projects))))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="print the line and leave the file alone")
    args = ap.parse_args()

    try:
        own = repos()
    except Blocked as exc:
        # Loud, and nothing written. The old number stays, which is stale but
        # true, rather than being replaced by a confident wrong one.
        print("  BLOCKED: %s" % exc, file=sys.stderr)
        print("  README not touched.", file=sys.stderr)
        return 2

    line = sentence(own)
    print("  %s" % line)
    if args.check:
        return 0

    page = io.open(README, encoding="utf-8").read()
    if START not in page or END not in page:
        print("  BLOCKED: no %s / %s markers in README.md" % (START, END),
              file=sys.stderr)
        return 2

    head, rest = page.split(START, 1)
    _, tail = rest.split(END, 1)
    io.open(README, "w", encoding="utf-8", newline="\n").write(
        head + START + "\n" + line + "\n" + END + tail)
    print("  README.md updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
