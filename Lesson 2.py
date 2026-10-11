# #PiSearch #IntegerArithmetic #FloorDivision #RepeatedHalving
ONE = 10**30
term = ONE//2 
total = 0
count = 0

while term > 0:
    total += term
    term = term//2
    count +=1

print(total//100)
print(count)
print(ONE-total)