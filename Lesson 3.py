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


print(arctan_inv(5, 10**50))
print(arctan_inv(239, 10**50))





#making arctan to get the digits of pi