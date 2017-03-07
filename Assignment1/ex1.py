import ddt, copy

#list of pairs message plaintext/ciphertext
tup_mess_ciphers = [
    [1, 0xe],
    [0xe, 9],
    [2, 6],
    [0xd, 0xa],
    [3, 7],
    [0xc, 0xb]
]

S = ddt.S
reverseS = {value : key for key, value in S.iteritems()}


def break_cipher_two(tup_mess_ciphers):
    # Initialize counters for key guesses
    keyCounters = {}
    for i in range(0, 0xf + 1):
        keyCounters[i] = 0

    # Combine messages/ciphertexts into all possible pairs
    mcPairs = []
    for i in range(0, len(tup_mess_ciphers)):
        for j in range(i + 1, len(tup_mess_ciphers)):
            a = tup_mess_ciphers[i]
            b = tup_mess_ciphers[j]
            mcPairs.append([a, b])
    for i in range(0, len(mcPairs)):
        for key_guess in keyCounters.keys():
            x0 = mcPairs[i][0][1] ^ key_guess
            x1 = mcPairs[i][1][1] ^ key_guess
            w0 = reverseS[x0]
            w1 = reverseS[x1]
            v0_xor_v1 = w0 ^ w1
            p0 = mcPairs[i][0][0]
            p1 = mcPairs[i][1][0]
            difference = p0 ^ p1

            maximum = 0
            entry_frequency = ddt.get_difference_table(S)[difference]
            for frequency in entry_frequency.values():
                if frequency > maximum:
                    maximum = frequency
            best_characteristic = 0
            for entry in entry_frequency.keys():
                if entry_frequency[entry] == maximum:
                    best_characteristic = entry
                    break


            if v0_xor_v1 == best_characteristic:
                keyCounters[key_guess] += 1

    return keyCounters

def break_cipher_one(k2, plainsCiphers):

    mess_ciphers_for_cipher_one = copy.deepcopy(plainsCiphers)

    for i in range(0, len(mess_ciphers_for_cipher_one)):
        plaintext = mess_ciphers_for_cipher_one[i][0]
        new_ciphertext = reverseS[mess_ciphers_for_cipher_one[i][1] ^ k2]
        mess_ciphers_for_cipher_one[i] = [plaintext, new_ciphertext]

    # Initialize counters for key guesses
    key_counters = {}
    for i in range(0, 0xf + 1):
        key_counters[i] = 0
    # Combine messages/ciphertexts into all possible pairs
    mc_pairs = []
    for i in range(0, len(mess_ciphers_for_cipher_one)):
        for j in range(i + 1, len(mess_ciphers_for_cipher_one)):
            a = mess_ciphers_for_cipher_one[i]
            print 'a = ' + str(a)
            b = mess_ciphers_for_cipher_one[j]
            mc_pairs.append([a, b])
    print "pairs" + str(mc_pairs)

    for i in range(0, len(mc_pairs)):
        u0_xor_u1 = mc_pairs[i][0][0] ^ mc_pairs[i][1][0]
        for key_guess in key_counters.keys():
            u = (reverseS[key_guess ^ mc_pairs[i][0][1]]) ^ (reverseS[key_guess ^ mc_pairs[i][1][1]])
            if u == u0_xor_u1:
                key_counters[key_guess] += 1

    return key_counters


# key_counts_for_k2 = break_cipher_two(tup_mess_ciphers)
#
# print 'Key counts for k2'
# print key_counts_for_k2

# assume k2 = 2 (from the counters)
k2 = 2
#
# key_counts_for_k1 = break_cipher_one(2, tup_mess_ciphers)
# print 'Key counts for k1'
# print key_counts_for_k1

#assume k1 = 7 (10 also possible, but check 7 first)
k1 = 7



#
# first_pair = tup_mess_ciphers[0]
# second_pair = tup_mess_ciphers[1]
# u = reverseS[reverseS[first_pair[1] ^ 2] ^ 7 ]
# k0 = first_pair[0] ^ u
# print 'Guess for k0 = ' + str(k0)