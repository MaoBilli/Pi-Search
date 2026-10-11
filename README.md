# Pi-Search

Search numbers or words in the first 100 MILLION digits of pi using Python.

Using Chudnovsky's algorithm, I was able to create a program which created 100 MILLION digits of pi in a single txt file.

No libraries needed: everything is plain Python (the standard library only).

## Files in this project

| File | What it is |
|---|---|
| `search.py` | **The search program.** Loads a file of pi digits and tells you if your number or word is in pi, where it first appears, and how many times. |
| `100m_pi_creator.py` | Makes **100,000,000** digits of pi with **Chudnovsky's formula** and saves them to `my_pi_100m.txt`. Checks the result against a SHA-256 fingerprint. |
| `1m_pi_creator.py` | Makes **1,000,000** digits of pi with **Machin's formula** (arctan) and saves them to `my_pi_1m.txt`. |
| `125k_pi_creator.py` | Makes **125,000** digits of pi with Machin's formula and saves them to `my_pi_125k.txt`. |
| `my_pi_125k.txt` | 125,000 digits of pi (about 125 KB). *Not included: make it with `125k_pi_creator.py`.* |
| `my_pi_1m.txt` | 1,000,000 digits of pi (about 1 MB). *Not included: make it with `1m_pi_creator.py`.* |
| `my_pi_100m.txt` | 100,000,000 digits of pi (about 100 MB). **Not included**: it is far over GitHub's 25 MB file limit for uploads, so I couldn't put it here. Make it with `100m_pi_creator.py`. |
| `word_to_number_function.py` | The word-to-digits function on its own (A=1, B=2, ... Z=26), written and tested separately before it went into `search.py`. |
| `Lesson 1.py`, `Lesson 2.py`, `Lesson 3.py` | The first steps I wrote while learning how to calculate pi (see [How I built it](#how-i-built-it)). |

> **Why aren't the `.txt` files here?** GitHub only lets you upload files up to 25 MB through its website, and the 100 million digit file is about 100 MB. So the digit files are not included in this repo. You make them yourself by running the creator files below (the 125,000 digit one takes about 10 seconds), and the fingerprints in [Check your digits](#check-your-digits) prove that yours are correct.

All digit files hold the digits **after the decimal point**, in one long line with no spaces. Digit 1 is the 1 in 3.14159...

## Example

```
number or word? number
What number(s) do you want to search pi for: 123456
First found at digit 2,458,885
There are 103 times where your number(s) have shown up, the first few digit places include [2458885, 3735793, 5472551, 5708040, 5846932]
```

```
number or word? word
What word do you want to search pi for: DAVID
Searching for the digits: 412294
First found at digit 206,399
There are 84 times where your number(s) have shown up, the first few digit places include [206399, 1331653, 1566431, 2935319, 5251782]
```

```
number or word? word
What word do you want to search pi for: MICHAEL
Searching for the digits: 139381512
Those digits were not found in the first 100,000,000 digits of pi
```

Some more results from the 100 million digits:

| Search | Digits searched | First found at digit | Times found |
|---|---|---|---|
| `999999` (the Feynman point) | 999999 | 762 | 107 |
| `1234567` | 1234567 | 9,470,344 | 9 |
| `8675309` | 8675309 | 9,202,591 | 7 |
| `0123456789` | 0123456789 | not found | 0 |
| EMMA | 513131 | 2,489,869 | 97 |
| JOHN | 1015814 | 3,218,948 | 10 |
| SARAH | 1911818 | 19,431,971 | 6 |
| HELLO | 85121215 | 34,851,875 | 2 |
| CLAUDE | 31212145 | 36,577,078 | 3 |
| MICHAEL | 139381512 | not found | 0 |

## Quick start

You need Python 3 (3.12 or newer is recommended, because turning a huge number into text is much faster there).

### 1. Get a file of digits

Pick one. The smaller ones are quick, so start there.

| Run this | You get | Method | Time |
|---|---|---|---|
| `python 125k_pi_creator.py` | `my_pi_125k.txt` (125,000 digits) | Machin | about 10 seconds |
| `python 1m_pi_creator.py` | `my_pi_1m.txt` (1,000,000 digits) | Machin | about 10 minutes (estimate) |
| `python 100m_pi_creator.py` | `my_pi_100m.txt` (100,000,000 digits) | Chudnovsky | **5 hours 20 minutes** (measured) |

The 100 million run took 19,190 seconds on a Surface Pro 11 (Snapdragon X Plus) with Python 3.14. It needs roughly 3 to 4 GB of free RAM and cannot be paused or resumed, so keep the computer plugged in and stop it from going to sleep. The other two times are estimates, so yours will vary.

### 2. Point the search at your file

At the top of `search.py`, change the file name in the `open(...)` line to the file you made:

```python
with open("my_pi_100m.txt", "r") as f:
```

(or `my_pi_1m.txt`, or `my_pi_125k.txt`).

### 3. Search

```
python search.py
```

Searching is very fast once the file is loaded: a million-digit file takes well under a millisecond to scan, and even a search with 10 million matches (like the single digit `7`) finishes in a couple of seconds.

## How the word search works

Pi only contains digits, so a word is turned into digits first, using **A=1, B=2, ... Z=26**. Each letter becomes its place in the alphabet and the numbers are joined together:

```
HI    ->  8, 9         ->  89
DAVID ->  4,1,22,9,4   ->  412294
```

Things to know:

- Letters like J (10) or Z (26) take two digits, so a 4-letter name is usually a 6 to 8 digit string.
- The numbers are joined with no gaps, so `12` could mean AB or L. A match tells you the *digits* are in pi. It does not mean pi spells your word.
- Capital letters, small letters, spaces and symbols are all handled: only the letters count.
- If you type something that isn't valid (a letter in a number search, or a word with no letters), the program asks you again.

## How likely is it that your number is in there?

For a random-looking string of n digits, the chance of it appearing somewhere in 100 million digits is about:

| Digits in your search | Chance it appears |
|---|---|
| 6 or fewer | about 100% |
| 7 | 99.995% |
| 8 | 63% |
| 9 | 9.5% |
| 10 | 1% |

Each extra digit makes it about ten times less likely. That's why short names are easy to find and long ones usually aren't. (Pi is believed, but not proven, to behave like a random string of digits.)

If you use the smaller files, the chances drop: in 1 million digits a 7-digit string only appears about 10% of the time.

## Check your digits

`100m_pi_creator.py` compares the SHA-256 fingerprint of your digits with known-correct ones. If they match, every digit is right.

| Digits | SHA-256 |
|---|---|
| 125,000 | `3f599bf5728319cc20299ec20d744d857f93e54118f57f7ec6ed7834e5484f3c` |
| 1,000,000 | `7806ee47461b49ef1f578e14461b2c83c09c6d7a9a914275da1d71e9cbbf7069` |
| 4,000,000 | `3b447adf831964fd071c07652456f1f4ff709d04af4be9caf81c41b642f566f9` |
| 10,000,000 | `c3d3dd4bd5d1051fd5995db983eb898ac0308189a20c46e80e5f67d5f415edf1` |
| 100,000,000 | `413258dd0311891fe0ea61ff843dfec5d3ce81155f5ac0a0baea41a03b3d18fe` |

The last 20 digits are:

| Digits | Last 20 digits |
|---|---|
| 125,000 | `95275957089861258677` |
| 1,000,000 | `22090106105779458151` |
| 100,000,000 | `14970581120187751592` |

To check the 125k or 1M files, which don't check themselves, run this (change the file name to match):

```python
import hashlib
with open("my_pi_1m.txt", "r") as f:
    print(hashlib.sha256(f.read().encode()).hexdigest())
```

## How it works

- **Whole numbers only.** Normal decimals (floats) are only accurate to about 16 digits, so everything is done with Python's unlimited-size integers, scaled up by a power of ten. A few extra "guard digits" are calculated and then thrown away, so rounding errors never reach the digits you keep.
- **Machin's formula** (`125k_pi_creator.py`, `1m_pi_creator.py`): `pi = 16 x arctan(1/5) - 4 x arctan(1/239)`. Each arctan is an alternating series that is added up in a loop. Simple, but it slows down fast: doubling the digits makes it about 4 times slower.
- **Chudnovsky's formula** (`100m_pi_creator.py`) adds about 14 correct digits of pi per term, compared with about 1.4 for arctan(1/5). With **binary splitting**, which adds up the terms by splitting the list in half again and again, 100 million digits becomes possible in plain Python.
- **Searching** uses Python's `str.find()`. To count matches that overlap (like `11` inside `111`), each search starts one place after the start of the last match, rather than after its end.

## How I built it

1. **`Lesson 1.py`**: working with whole numbers instead of decimals, by scaling everything up by a power of ten (for example, the first 50 digits of 1/13).
2. **`Lesson 2.py`**: adding up a series in a loop, and seeing how rounding down loses a tiny bit each time, which is why guard digits are needed.
3. **`Lesson 3.py`**: the arctan series as a function, `arctan_inv(x, ONE)`.
4. **Digit makers**: pi from two arctans (125,000 and 1,000,000 digits), then Chudnovsky for 100,000,000.
5. **Search**: number or word search, retry on bad input, counting overlapping matches.

## Credits

Built while learning Python, with help from Claude (an AI assistant made by Anthropic), including the Chudnovsky implementation.
