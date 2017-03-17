from random import randint

# output True for probable prime, False for surely composite (m: number to test, k: test accuracy)
def Miller_Rabin_Test(m, k):
    if m == 2 or m == 3: return True
    if m % 2 == 0: return False # even m is clearly NOT a prime
    # Let m - 1 = 2^s*t, t odd
    n = m - 1
    countDivisions = 0
    while n % 2 == 0:
        n /= 2
        countDivisions += 1
    s = countDivisions
    t = (m-1)/pow(2, s)

    for _ in range(k):
        #Pick a random b
        b = randint(2, m - 1)
        #Compute y = b^t mod m
        y = pow(b, t, m)
        if y == 1 or y == m - 1:
            continue
        i = 1
        for i in range(s + 1):
            y = pow(y, 2, m)
            if y == 1: return False
            elif y == m - 1:
                break #continue outer loop here
        if i == s: #if the previous loop has run all the iterations
            return False
    return True


#test!
print str(Miller_Rabin_Test(221, 2))
counter = 0
for i in range(20, 30001):
    result = Miller_Rabin_Test(i, 3)
    if result == True :
        counter += 1
        print str(i) + ' is a probable prime'
    else:
        print str(i) + ' is surely composite'
print counter