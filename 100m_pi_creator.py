# =====================================================================
#  Make millions of digits of pi with Chudnovsky's formula (plain Python)
#  Change DIGITS below. Try 1_000_000 first, then 10_000_000, then 100_000_000.
# =====================================================================
import math
import sys
import time
import hashlib

sys.set_int_max_str_digits(0)     # let Python turn huge numbers into text

DIGITS = 100_000_000                # how many digits AFTER the decimal point you want
GUARD = 30                        # extra digits we calculate, then throw away (rounding safety)

# "Fingerprints" (SHA-256) of the CORRECT digits, so you can check your answer.
# If your fingerprint matches, every single digit is right.
CHECKSUMS = {
    1_000_000:   "7806ee47461b49ef1f578e14461b2c83c09c6d7a9a914275da1d71e9cbbf7069",
    4_000_000:   "3b447adf831964fd071c07652456f1f4ff709d04af4be9caf81c41b642f566f9",
    10_000_000:  "c3d3dd4bd5d1051fd5995db983eb898ac0308189a20c46e80e5f67d5f415edf1",
    100_000_000: "413258dd0311891fe0ea61ff843dfec5d3ce81155f5ac0a0baea41a03b3d18fe",
}

C3_OVER_24 = 640320 ** 3 // 24


def split(a, b):
    """Adds up the formula's terms a to b-1 by splitting the range in half again and again.
    This 'binary splitting' trick is what makes it so much faster than your arctan loop."""
    if b - a == 1:                                   # just one term: work it out directly
        if a == 0:
            p = q = 1
        else:
            p = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            q = a * a * a * C3_OVER_24
        t = p * (13591409 + 545140134 * a)
        if a % 2 == 1:                               # the terms alternate between + and -
            t = -t
        return p, q, t
    mid = (a + b) // 2                               # split the range into two halves...
    p1, q1, t1 = split(a, mid)
    p2, q2, t2 = split(mid, b)
    return p1 * p2, q1 * q2, q2 * t1 + p1 * t2       # ...and glue the two answers together


start = time.time()

def stamp(message):
    print(f"[{time.time() - start:9.1f}s] {message}", flush=True)


precision = DIGITS + GUARD
terms = int(precision / 14.181647462725477) + 2      # each term gives about 14.18 digits

stamp(f"Step 1 of 4: adding up {terms:,} terms (this is the long part)...")
p, q, t = split(0, terms)
del p                                                # we don't need this one any more (frees memory)

stamp("Step 2 of 4: square root...")
one = 10 ** precision                                # the big whole number that stands for 1
root = math.isqrt(10005 * one * one)                 # square root of 10005, scaled up
del one

stamp("Step 3 of 4: final division...")
pi_scaled = (q * 426880 * root) // t
del q, t, root

stamp("Step 4 of 4: turning the number into text...")
text = str(pi_scaled)                                # starts with the 3, then the decimals
del pi_scaled
digits_text = text[1:DIGITS + 1]                     # drop the "3", keep DIGITS digits, drop the guard digits
del text

filename = f"my_pi_{DIGITS // 1_000_000}m.txt"
stamp(f"Saving to {filename} ...")
with open(filename, "w") as f:
    f.write(digits_text)

print()
print("digits saved:  ", f"{len(digits_text):,}")
print("first 20:      ", digits_text[:20])
print("last 20:       ", digits_text[-20:])

fingerprint = hashlib.sha256(digits_text.encode()).hexdigest()
print("fingerprint:   ", fingerprint)
if DIGITS in CHECKSUMS:
    if fingerprint == CHECKSUMS[DIGITS]:
        print("CHECK: MATCH - every digit is correct!")
    else:
        print("CHECK: MISMATCH - something went wrong, do not trust this file")
else:
    print("CHECK: no stored fingerprint for this size")
stamp("Done.")