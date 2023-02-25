import numpy as np

Rows = int(input("Enter the number of rows: "))
Columns = int(input("Enter the number of columns: "))

print("------Please write the elements of the matrix in a single line----")

elements = list(map(int, input().split()))

key = np.array(elements).reshape(Rows, Columns)

plaintext = str(input('Enter the plaintext in lowercase: '))


plaintext_nums = [ord(c)-ord('a') for c in plaintext]

if len(plaintext_nums) % 2 !=0:
    plaintext_nums.append(0)

plaintext_groups = [plaintext_nums[i:i+2] for i in range(0, len(plaintext_nums), 2)]

ciphertext_groups = []
for groups in plaintext_groups:

    group_matrix = [[groups[0]], [groups[1]]]

    ciphertext_matrix = [[0],[0]]

    for i in range(2):
        for j in range(2):
            ciphertext_matrix[i][0] += key[i][j] * group_matrix[j][0]
            ciphertext_matrix[i][0] %= 26

    ciphertext_group = [ciphertext_matrix[i][0] for i in range(2)]

    ciphertext_groups.append(ciphertext_group)

ciphertext = ''.join([chr(c + ord('a')) for group in ciphertext_groups for c in group])

print("Ciphertext:")
print(ciphertext)