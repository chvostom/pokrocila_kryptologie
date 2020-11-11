#!/usr/bin/python3

__author__      = "Tomas Zvara, Tomas Fornusek, Robert Lorencz, Jiri Bucek"

import argparse
from spn import encrypt, substitution_dec

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

def linear_cryptoanalysis(pt_file, ct_file, pmask, umask, key_mask, bias):
    key_byte1, key_byte2 = extract_key_bytes(key_mask)

    hit_table = [0] * (2**(16))
    max_hit_table = [{'key':0,'bias': 0,'Q':1} for i in range(0,20)] #key, bias, Q

    count = 0
    with open(pt_file, 'r') as fid_pt, open(ct_file, 'r') as fid_ct:
        for ot_block,ct_block in zip(fid_pt.read().split(), fid_ct.read().split()):
            ot_block = int(ot_block, 16)
            ct_block = int(ct_block, 16)

            ot_masked = ot_block & pmask
            ot_hamming = hamming_weight(ot_masked)

            for k in range(0,16):
                for i in range(0,16):
                    key = (k << key_byte2) | (i << key_byte1)
                    U = reverse_last_round(ct_block,key) & umask
                    Uxor = ot_hamming + hamming_weight(U)
                    if (Uxor % 2) == 0:
                        hit_table[key]+=1
            count+=1

        for k in range(0,16):
            for i in range(0,16):
                key = (k << key_byte2) | (i << key_byte1)
                hit_table[key] = abs((hit_table[key] - (count/2))/count)
                Q = abs(bias - hit_table[key])
                #save the maximum
                if Q < max_hit_table[-1]['Q']:
                    max_hit_table[-1]['key'] = key
                    max_hit_table[-1]['bias'] = hit_table[key]
                    max_hit_table[-1]['Q'] = Q
                    max_hit_table = sorted(max_hit_table, key=lambda x: x['Q'], reverse=False)
    return max_hit_table

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plaintext", help="plaintext file")
    parser.add_argument("ciphertext", help="ciphertext file")
    args = vars(parser.parse_args())

    # %%%%%% DEFAULT ARGS %%%%%% #
    P_mask = 0b0100000000000100 #Plaintext bitmask
    U_mask = 0b1000000010000000 #U mask
    key_mask = 0b1010 #Sbox mask - !!!max 2 ones!!!
    bias = 1/64

    print(f"Predicted bias: {bias:.4f}")
    
    max_hits = linear_cryptoanalysis(args['plaintext'], args['ciphertext'], P_mask, U_mask, key_mask, bias)

    print("Top 20 biases:")
    for res in max_hits:
        print(f"Key: 0x{res['key']:04X}, bias: {res['bias']:.4f}")

if __name__ == "__main__":
    main()
