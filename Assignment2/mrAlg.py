from random import randint


def miller_rabin_test(m, k):
    """Miller Rabin primality test

    :param m: number to test
    :param k: test accuracy
    :return: True for probable prime, False for surely composite
    """
    if m == 2 or m == 3: return True
    if m % 2 == 0: return False  # even m is clearly NOT a prime

    # Let m - 1 = 2^s*t, t odd
    n = m - 1
    count_divs = 0
    while n % 2 == 0:
        n /= 2
        count_divs += 1
    s = count_divs
    t = (m - 1) / pow(2, s)

    for _ in range(k):
        # Pick a random b
        b = randint(2, m - 1)
        # Compute y = b^t mod m
        y = pow(b, t, m)
        if y == 1 or y == m - 1:  # m could be prime, go for another random b
            continue
        i = 1
        for i in range(s + 1):
            y = pow(y, 2, m)
            if y == 1:
                return False
            elif y == m - 1:
                break  # continue outer loop here
        if i == s:  # if the previous loop has run all the iterations
            return False
    return True




# print str(miller_rabin_test(221, 2))
counter = 0
for i in range(20, 30000 + 1):
    result = miller_rabin_test(i, 3)
    if result:
        counter += 1
        print str(i) + ' is a probable prime'
    else:
        print str(i) + ' is surely composite'
print counter

# There are 3237 primes between 20 and 30,000

