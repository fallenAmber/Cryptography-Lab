import string

def polyalphabeticENCRYPTION(plaintext,key):

    keyword=""

    while len(keyword)<len(plaintext):
        keyword=keyword+key

    keyword=keyword[:len(plaintext)]

    ciphertext=""

    for i,letter in enumerate(plaintext.lower()):

        if letter in string.ascii_lowercase:
            key_letter = keyword[i]

            key_index = string.ascii_lowercase.index(key_letter)

            plaintext_index = string.ascii_lowercase.index(letter)

            ciphertext_index = (key_index + plaintext_index) % 26

            ciphertext += string.ascii_lowercase[ciphertext_index]

        else:
            ciphertext += letter

    return ciphertext

def polyalphabeticDECRYPTION(ciphertext,key):

    keyword=""

    while len(keyword)<len(ciphertext):
        keyword=keyword+key

    keyword=keyword[:len(ciphertext)]


    text=""

    for i,letter in enumerate(ciphertext.lower()):

        if letter in string.ascii_lowercase:
            key_letter = keyword[i]

            key_index = string.ascii_lowercase.index(key_letter)

            ciphertext_index = string.ascii_lowercase.index(letter)

            org_index = ( ciphertext_index - key_index) % 26

            text += string.ascii_lowercase[org_index]

        else:
            text += letter

    return text


plaintext = "wearediscoveredsaveyourself"
key = "deceptive"
ciphertext = polyalphabeticENCRYPTION(plaintext, key)
org_text = polyalphabeticDECRYPTION(ciphertext,key)
print(ciphertext)
print(org_text)
