def ext_euc_alg(a, b):
    if b == 0: return a, 1, 0
    rem1, s1, t1 = ext_euc_alg(b, a % b)
    rem = rem1
    s = t1
    t = s1 - (a/b) * t1
    return rem, s, t


gcd, s, t = ext_euc_alg(3, 404800)
print 'Inverse of 3 mod 404800 is: '
inv = s % 404800
print inv #  d1 = 269867

gcd2, s2, t2 = ext_euc_alg(3, 20240)
print 'Inverse of 3 mod 20240 is: '
inv2 = s2 % 20240
print inv2 #  d2 = 6747