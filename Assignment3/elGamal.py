from random import randint

p = 2189284635404723        # prime to use as modulo
alpha = 2                   # primitive element of p
a = randint(2, p-3)         # some valid private key
beta = pow(alpha, a, p)     # beta=alpha^a mod p
k = 1234567                 # some random k
m = 162870                  # message m
n = 2051152801041163        # n used for hashing (8^m mod n)

# ONLY for the case p=2q+1 (p, q primes)
def is_primitive_element(alpha):
    one = (p - 1) / 2
    two = 2
    if pow(alpha, one, p) != 1 and pow(alpha, two, p) != 1:
        return True
    return False

def are_congruent(a, b, n):
    if pow(a, 1, n) == pow(b, 1, n):
        return True
    return False

def ext_euc_alg(a, b):
    if b == 0: return a, 1, 0
    rem1, s1, t1 = ext_euc_alg(b, a % b)
    rem = rem1
    s = t1
    t = s1 - (a/b) * t1
    return rem, s, t

def calculate_signature(m):
    x = pow(8, m, n) # calculating hash of a message
    gamma = pow(alpha, k, p)
    gcd, sss, t = ext_euc_alg(k, p-1) # use eea to find multiplicative inverse of k mod p-1
    k_inverse = sss % (p-1)
    delta = (x-(a*gamma))*k_inverse % (p-1)
    return gamma, delta, x

our_gamma, our_delta, our_x = calculate_signature(m)

print 'gamma'
print our_gamma
print 'delta'
print our_delta
print 'private key a'
print a

checkOne = pow(pow(beta, our_gamma, p) * pow(our_gamma, our_delta, p), 1, p)
checkTwo = pow(alpha, our_x, p)

print 'check one is'
print checkOne
print 'check two is'
print checkTwo

checkThree = are_congruent(checkOne, checkTwo, p)
print 'Signature is valid: '
print checkThree