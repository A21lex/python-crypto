import math

def trial_division(m):
    if m % 2 == 0: return False
    for r in range (2, int(math.sqrt(m)) + 1):
        if m % r == 0:
            return False
    return True


counter = 0
for i in range(20, 30000+1):
    result = trial_division(i)
    if result:
        counter += 1
        print str(i) + ' is a prime'
    else:
        print str(i) + ' is composite'
print counter