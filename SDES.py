
def permute(key,perm):

    return "".join(key[i-1] for i in perm)

def shift(key,shift):

    return key[shift:]+key[:shift]


def generate_subkeys(key):

    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]

    key = permute(key, p10)

    left = key[:5]
    right = key[5:]

    k1=[]
    k2=[]

    left_sided_shift1 = shift(left,1)
    right_sided_shift1 = shift(right,1)

    shifted_key1 = left_sided_shift1+right_sided_shift1

    subkey1 = permute(shifted_key1, p8)

    k1.append(subkey1)

    left_sided_shift2 = shift(left_sided_shift1,2)
    right_sided_shift2 = shift(right_sided_shift1,2)
    shifted_key2 = left_sided_shift2 + right_sided_shift2
    subkey2 = permute(shifted_key2, p8)
    k2.append(subkey2)

    return k1, k2

key = "1010000010"

p = generate_subkeys(key)

print(f"k1, k2  : {p}")

#finishing key generation



"""

# Key generation functions

def permute(key, perm):
    return ''.join(key[i - 1] for i in perm)

def shift(key, shift):
    return key[shift:] + key[:shift]

def generate_subkeys(key):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]

    # Apply P10 permutation
    key = permute(key, p10)

    # Split key into two halves
    left = key[:5]
    right = key[5:]

    subkeys = []

    # Generate 2 subkeys
    for shift in [1, 2]:
        # Shift each half
        left_shifted = shift(left, shift)
        right_shifted = shift(right, shift)

        # Combine and apply P8 permutation
        subkey = permute(left_shifted + right_shifted, p8)
        subkeys.append(subkey)

    return subkeys

# Encryption and decryption functions

def f(k, r):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    p4 = [2, 4, 3, 1]
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

    # Expand R to 8 bits using EP permutation
    r = permute(r, ep)

    # XOR with key
    r = '{0:08b}'.format(int(r, 2) ^ int(k, 2))

    # Split into two 4-bit halves
    left = r[:4]
    right = r[4:]

    # S-box lookup
    s0_row = int(left[0] + left[3], 2)
    s0_col = int(left[1] + left[2], 2)
    s0_val = '{0:02b}'.format(s0[s0_row][s0_col])

    s1_row = int(right[0] + right[3], 2)
    s1_col = int(right[1] + right[2], 2)
    s1_val = '{0:02b}'.format(s1[s1_row][s1_col])

    # Combine and apply P4 permutation
    result = permute(s0_val + s1_val, p4)

    return result

def encrypt(plaintext, key):
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    inv_ip = [4, 1, 3, 5, 7, 2, 8, 6]

    subkeys = generate_subkeys(key)

    # Apply initial permutation (IP)
    ciphertext = permute(plaintext,ip)"""