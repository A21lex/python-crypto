import ddt, copy, ex1

#list of pairs message plaintext/ciphertext
tup_mess_ciphers = [
    [0,1],[1,0xd],[2,8],[3,0xa],[4,4],[5,3],[6,0],[7,2],
    [8,0xf],[9,6],[0xa,0xe],[0xb,0xc],[0xc,5],[0xd,0xb],[0xe,7],[0xf,9]
]

S = ddt.S
reverseS = {value : key for key, value in S.iteritems()}


def break_cipher_three(tup_mess_ciphers):
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
            best_characteristic_round_one = 0
            for entry in entry_frequency.keys():
                if entry_frequency[entry] == maximum:
                    best_characteristic_round_one = entry
                    break
            best_characteristic_round_two = 0
            maximum_two = 0
            entry_frequency_two = ddt.get_difference_table(S)[best_characteristic_round_one]
            for frequency in entry_frequency_two.values():
                if frequency > maximum_two:
                    maximum_two = frequency
            for entry in entry_frequency_two.keys():
                if entry_frequency_two[entry] == maximum_two:
                    best_characteristic_round_two = entry
                    break

            if v0_xor_v1 == best_characteristic_round_two:
                keyCounters[key_guess] += 1

    return keyCounters




key_counts_for_k3 = break_cipher_three(tup_mess_ciphers)

print 'Key counts for k3'
print key_counts_for_k3

#assume k3 = 6 (from the counters)
k3 = 6
print 'k3 is assumed to be: ' + str(k3)


#transform the ciphertexts to transform cipherThree into cipherTwo

new_list_mess_ciphers = copy.deepcopy(tup_mess_ciphers)
for i in range(0, len(new_list_mess_ciphers)):
    plaintext = new_list_mess_ciphers[i][0]
    new_ciphertext = reverseS[new_list_mess_ciphers[i][1] ^ k3]
    new_list_mess_ciphers[i] = [plaintext, new_ciphertext]

key_counts_for_k2 = ex1.break_cipher_two(new_list_mess_ciphers)

print 'Key counts for k2'
print key_counts_for_k2

#assume k2 = 3 (from the counters)
k2 = 3
print 'k2 is assumed to be: ' + str(k2)
key_counts_for_k1 = ex1.break_cipher_one(k2, new_list_mess_ciphers)

print 'Key counts for k1'
print key_counts_for_k1
#assume k1 = 4 (from the counters)
k1 = 4
print 'k1 is assumed to be: ' + str(k1)

first_pair = tup_mess_ciphers[0]
second_pair = tup_mess_ciphers[1]
u = reverseS[reverseS[reverseS[first_pair[1] ^ k3] ^ k2 ] ^ k1]
k0 = first_pair[0] ^ u
print 'Guess for k0 = ' + str(k0)

print 'The keys are: '
print k0, k1, k2, k3