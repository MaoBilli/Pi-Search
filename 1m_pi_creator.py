# #PiSearch #MachinFormula #FixedPointArithmetic #GuardDigits #LargeIntegers
import sys

sys.set_int_max_str_digits(0)

def arctan_inv(x,ONE):
    n = 1
    total = 0
    sign = 1
    power = ONE//x
    while power > 0:
        total += sign * (power//n)
        power = power // (x*x)
        n += 2
        sign *= -1
    return(total)

DIGITS = 1_000_000
GUARD = 20
ONE = 10**(DIGITS + GUARD)
import time 
start = time.time()
pi_scaled = 16 * arctan_inv(5, ONE) - 4 * arctan_inv(239, ONE)
pi_text = str(pi_scaled)
pi_text = pi_text[:-GUARD]
print(time.time() - start)
print(len(pi_text))
print(pi_text[999981:1000001])

with open("my_pi.txt", "w") as f:
    f.write(pi_text[1:])
print("saved",len(pi_text[1:]))