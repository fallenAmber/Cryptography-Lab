
def create_matrix(key):

    #Alternate way of matrix creation

    """def create_matrix(key):
    key = key.upper()
    matrix = [['' for x in range(5)] for y in range(5)]
    letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.replace('J', 'I')
    key += letters

    for i in range(5):
        for j in range(5):
            matrix[i][j] = key[i*5 + j]

    return matrix"""


    key = key.upper()
    matrix = [[0 for i in range(5)] for i in range(5)]
    letters_added = []

    row = 0
    column = 0

    for letter in key:

        if letter not in letters_added:
            matrix[row][column ] =letter
            letters_added.append(letter)
        else:
            continue

        if column==4:
            column =0
            row =row +1
        else:
            column =column +1


    for letter in range(65 ,91):

        if letter ==74:
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))

    index =0

    for i in range(5):

        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    return matrix

def add_fillers(message):

    index = 0

    while(index<len(message)):

        l1 = message[index]

        if (index == len(message)-1):

            message = message+'X'

            index = index+2

            continue
        l2 = message[index+1]

        if l1==l2:

            message = message[:index+1]+'X'+message[index+1:]

        index = index+2

    return message

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace('J', 'I')
    plaintext = plaintext.replace(' ', '')
    if len(plaintext) % 2 == 1:
        plaintext += 'X'

    matrix = create_matrix(key)

    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]

        a_row, a_col, b_row, b_col = 0, 0, 0, 0
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == a:
                    a_row, a_col = row, col
                elif matrix[row][col] == b:
                    b_row, b_col = row, col

        if a_row == b_row:
            a_col = (a_col + 1) % 5
            b_col = (b_col + 1) % 5
        elif a_col == b_col:
            a_row = (a_row + 1) % 5
            b_row = (b_row + 1) % 5
        else:
            a_col, b_col = b_col, a_col

        ciphertext += matrix[a_row][a_col]
        ciphertext += matrix[b_row][b_col]

    return ciphertext

key = str(input("Enter the key: "))

message = str(input("Enter the message: "))

encryption= encrypt(message,key)

print(encryption)






