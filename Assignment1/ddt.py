
#S-box
S = {0:6,
     1:4,
     2:0xc,
     3:5,
     4:0,
     5:7,
     6:2,
     7:0xe,
     8:1,
     9:0xf,
     0xa:3,
     0xb:0xd,
     0xc:8,
     0xd:0xa,
     0xe:9,
     0xf:0xb}

def get_v0_xor_v1(u0, differential, Sbox):
    "Given a u0, calculate v0^v1, assuming u0^u1=differential (Chosen plaintext attack)"
    u1 = u0 ^ differential
    v0 = Sbox[u0]
    v1 = Sbox[u1]
    return v0 ^ v1

def get_frequencies(table):
    "Count occurences of every value for u0 - v0xorv1 type table (for a single differential)"
    frequencyMap = {}
    for i in range(0, 0xf+1, 1):
        frequencyMap[i] = 0
    for val in table.values():
        count = 0
        for val2 in table.values():
            if (val == val2):
                count += 1
        frequencyMap[val] = count
    #print 'frMapBeforeReturn'
    #print frequencyMap
    return frequencyMap

def get_difference_table(Sbox):
    differenceTable = {}
    for differential in range(0, 0xf+1, 1):
        tableForOne = {}
        for u0 in range(0, 0xf+1, 1):
            tableForOne[u0] = get_v0_xor_v1(u0, differential, Sbox)
        frequencyMap = get_frequencies(tableForOne)
        differenceTable[differential] = frequencyMap
    return differenceTable

print 'Printing difference map'
differenceTable = get_difference_table(S)
for key in differenceTable.keys():
    print
    for i in range(0, 0xf+1, 1):
        print str(differenceTable[key][i]),



