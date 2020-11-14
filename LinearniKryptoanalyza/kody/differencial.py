#!/usr/bin/python3

__author__      = "Tomas Zvara, Tomas Fornusek, Robert Lorencz, Jiri Bucek"

import argparse
from spn import encrypt,substitution_dec

def extract_key_bytes(key_mask):
    res = []
    for byte in range(0,4):
        if(((key_mask >> byte) % 2) == 1):
            res.append(byte*4)
    return res

def hamming_weight(bits):
#Brian Kernighan's algorithm
    count = 0
    while bits:
        bits = bits & (bits - 1)
        count += 1
    return count

def reverse_last_round(block, key):
    return substitution_dec(block ^ key)

def differencial_cryptoanalysis(enc_key, size, deltaP, expected_deltaU4, key_mask, bias):
    key_byte1, key_byte2 = extract_key_bytes(key_mask)

    pt_1 = [i+1 for i in range(size)]
    pt_2 = [i^deltaP for i in pt_1]
    ct_1 = [encrypt(i,enc_key) for i in pt_1]
    ct_2 = [encrypt(i,enc_key) for i in pt_2]

    hit_table = [0] * (2**(16))
    max_hit_table = [{'key':0,'bias': 0,'Q':1} for i in range(20)] #key, bias, Q

    count = 0
    for n in range(size):
        for k in range(16):
            for i in range(16):
                key = (k << key_byte2) | (i << key_byte1)
                U1 = reverse_last_round(ct_1[n],key)
                U2 = reverse_last_round(ct_2[n],key)
                deltaU = U1 ^ U2
                if deltaU == expected_deltaU4:
                    hit_table[key]+=1
        count+=1

    for k in range(16):
        for i in range(16):
            key = (k << key_byte2) | (i << key_byte1)
            hit_table[key] = abs(hit_table[key]/count)
            Q = abs(bias - hit_table[key])
            #save the maximum
            if Q < max_hit_table[-1]['Q']:
                max_hit_table[-1]['key'] = key
                max_hit_table[-1]['bias'] = hit_table[key]
                max_hit_table[-1]['Q'] = Q
                max_hit_table = sorted(max_hit_table, key=lambda x: x['Q'], reverse=False)

    return max_hit_table

def main():
    # %%%%%% DEFAULT ARGS %%%%%% #
    enc_key=0x1345 #key for encryption - normally, this is unknown, and not used later
    size = 5000 #number of plaintext block generated
    deltaP = 0b0000101100000000 #what bits differ at P
    expected_deltaU4 = 0b0000011000000110 #what bits must differ at U4
    key_mask = 0b0101 #Sbox mask - !!!max 2 ones!!!
    bias = 27/1024

    max_hits = differencial_cryptoanalysis(enc_key, size, deltaP, expected_deltaU4, key_mask, bias)

    print("Top 20 biases:")
    for res in max_hits:
        print(f"Key: 0x{res['key']:03X}, bias: {res['bias']:.4f}")

if __name__ == "__main__":
    main()