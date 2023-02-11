
def encrypt(text, shift):
    """Encrypt the string and return the ciphertext"""
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(cipher, shift):
    """Decrypt the string and return the original text"""
    text = ''
    for char in cipher:
        if char == ' ':
            text = text + char
        elif char.isupper():
            text = text + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            text = text + chr((ord(char) - shift - 97) % 26 + 97)
    return text


text = str(input('Enter the text: '))

shift = int(input('Input the key: '))

CT = encrypt(text, shift)

OM = decrypt(CT,shift)

print(CT)
print(OM)

