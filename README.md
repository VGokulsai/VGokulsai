## Gokul Sai

15, Hyderabad. I build small tools, and none of them will tell you a check
passed when it never ran.

<!-- stats:start -->
Twelve public repos, all written on my own, of which eleven are projects and one is this profile.
<!-- stats:end -->

Two of them are live: **[the journal](https://gokulsai1004-create.github.io/journal/)**
and **[Out Baby Out](https://gokulsai1004-create.github.io/outbabyout/)**.

### What I've shipped

**[painpoint-finder](https://github.com/gokulsai1004-create/painpoint-finder)** —
describe what you want to build and it searches six public sources for people
who actually have that problem, pulls out whoever already shipped it, and drafts
an opener you edit and send yourself. It never sends anything. 126 tests.

**[firstwrong](https://github.com/gokulsai1004-create/firstwrong)** — tells you
the first line of your homework working that is wrong, and nothing else. No
solution, no hint. The model has to solve it internally to compare, but only
three values are ever read out of its reply, so the answer is unreachable in the
code rather than politely withheld. 44 test cases: 25 of 25 on ordinary
problems, 16 of 19 on a hard set written blind against it.

**[synth](https://github.com/gokulsai1004-create/synth)** — turns a research
paper into a summary where every claim carries its page number, then checks that
page. Not whether the claim is true, only whether it can be found where it says.
Nothing in it can mark a claim false, so nothing does. One file, no
dependencies, $0.0017 a call.

**[apisurface](https://github.com/gokulsai1004-create/apisurface)** — what
actually changed in an npm package's public API, read from the published code
rather than from a changelog nobody wrote.

**[Out Baby Out](https://gokulsai1004-create.github.io/outbabyout/)** —
real-life tag with a revive, so nobody is ever out for good. The rules, a live
match console that enforces them while you play, and a field map you can put
anywhere. The rules exist in Python and in JavaScript, so twelve tests lift the
JavaScript out of the page and check the two still agree.

### The idea I keep running into

A source that searched and found nothing, and a source that was refused and
never looked, both return zero. They mean opposite things.

Getting that wrong lets a tool tell someone their real problem is imaginary. It
is harder than it sounds — DuckDuckGo refuses you with HTTP 202, a *success*
code. Stack Exchange does it two different ways. Each one parses as "the parser
is broken" if you check the body before the status.

Then I went looking for it in my own repos and **found it in five of them,
including inside the tool I built to catch it.** `firstwrong` printed "No wrong
line found" any time the model's answer could not be read, which is a pass, in a
tool whose only job is to catch a wrong answer.

Fixed all five and left 124 tests behind, every one proved by breaking the code
first and confirming the test failed. Two of the tests I wrote were passing
without testing anything. A passing test means nothing until you have watched it
fail. [I wrote the whole thing up
here.](https://gokulsai1004-create.github.io/journal/e/the-bug-was-in-the-tool-i-built-to-find-it)

### Eight ideas I killed before building them

- Gathered **992 posts** about a product I had prototyped. Money problems
  appeared 879 times. My idea appeared 7. Dead in four days instead of six
  months.
- Screened **963 more** for a second one. Same answer.
- Measured Bluetooth signal strength for a tag game before writing any of it.
  With the laptop and the beacon both completely still, 145 readings spanned
  **35 dBm**, while two beacons at genuinely different distances differed by 8.
  So a single reading cannot tell two metres from ten, and the design in my head
  could not work. That cost an afternoon instead of a month.

Five of the things I have shipped came from my own life. None of the eight dead
ones did.

### Now

Working through CS50. Building an agent that warns students about deadlines
early enough to prepare, with someone my own age. Writing up what breaks, in
[the journal](https://gokulsai1004-create.github.io/journal/).

📫 gokulsai1004@gmail.com  ·  [Instagram](https://instagram.com/gokulsai_2010)
