def euc_alg(a, b):
    if b > a:
        a, b = b, a
    rem = 0
    while not b == 0:
        rem = a % b
        if rem == 0: return b
        a = b
        b = rem
    return rem


aa = euc_alg(880, 460)
print aa