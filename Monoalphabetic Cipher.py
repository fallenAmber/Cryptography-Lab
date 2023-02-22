def encryption(plaintext,key):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    mapping = {alphabet[i]:key[i] for i in range(len(alphabet))}

    ciphertext=''

    for char in plaintext:

        if char.isalpha():

            if char.islower():

                ciphertext += mapping[char].lower()
            else:
                ciphertext += mapping[char.lower()].upper()

        else:

            ciphertext+=char

    return ciphertext

def decryption(plaintext,key):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    mapping = {key[i]:alphabet[i] for i in range(len(alphabet))}

    original=''

    for char in plaintext:

        if char.isalpha():

            if char.islower():

                original += mapping[char].lower()
            else:
                original += mapping[char.lower()].upper()

        else:

            original+=char

    return original


#plaintext = "The quick brown fox jumps over the lazy dog"

plaintext = str(input("Enter the message: "))
key = "qwertyuiopasdfghjklzxcvbnm"
ciphertext = encryption(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decryption(ciphertext, key)
print("Decrypted Plaintext:", decrypted_plaintext)