
import random

def gcd(a,b):

    while b!=0:

        a,b = b, a%b

    return a

def generate_key_pair(p,q):

    n = p*q

    phi = (p-1)*(q-1)

    e= random.randrange(1,phi) #genrerating public key

    g = gcd(e, phi)

    while g!=1:

        e = random.randrange(1,phi)

        g = gcd(e,phi)

    print("The Public key is: ", e)

    k = 1
    while True:
        d = (1 + (k * phi)) / e
        if d == int(d):
            break
        else:
            k += 1
    print("K is: ", k)
    print("The private key is: ", int)

    return ((e, n), (int(d), n))

def encrypt(public_key,text):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

def decrypt(private_key,ctext):

    key, n = private_key
    text = [chr(pow(char, key, n)) for char in ctext]
    return "".join(text)


p = int(input(" Enter a prime number: "))
q = int(input(" Enter another prime number (Not the one entered above): "))

public_key, private_key = generate_key_pair(p,q)
print("Public: ", public_key)
print("Private: ", private_key)

"""with open ('message.txt','r') as file:
    message = file.read()"""

message = str(input("Enter the message: "))

encrypted_msg = encrypt(public_key, message)

print("Encrypted message: ", ''.join(map(lambda x: str(x), encrypted_msg)))

print(" Original message: ", decrypt(private_key, encrypted_msg))





"""import random

max_PrimLength = 1000000000000

def gcd (a,b):

    while b!=0:

        a,b = b, a%b
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def is_prime(a):

    if a==2:
        return True
    if a<2 or a%2==0:
        return False
    for n in range(3, int(a**0.5)+2,2):

        if a%n==0:
            return False
    return True

def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Sorry, both numbers must be prime!')
    elif p == q:
        raise ValueError('Sorry, p and q cannot be equal!')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    e = random.randrange(1,phi)

    print("The public key is: ", e)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Extended Euclid's Algorithm for generating the private key
    d =multiplicative_inverse(e, phi)

    # Returning public and private key_pair
    return ((e, n), (d, n))

def encrypt(public_key,text):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

def decrypt(private_key,ctext):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

if __name__ == '__main__':

    p = int(input(" - Enter a prime number: "))
    q = int(input(" - Enter another prime number (Not the one entered above): "))

    print(" - Generating your public / private key-pairs now . . .")
    public_key, private_key = generate_key_pair(p,q)
    print("Public: ", public_key)
    print("Private: ", private_key)

    with open ('msg.txt','r') as file:
        message = file.read()
    message ="HI"

    encrypted_msg = encrypt(public_key, message)

    print(" - Encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))

    print(" - Decrypting message with private key ", private_key, " . . .")
    print(" - Original message is: ", decrypt(private_key, encrypted_msg))"""

