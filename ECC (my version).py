

p = int(input("Enter P:"))
a = int(input("Enter a:"))
b = int(input("Enter b:"))

listLHS = []
listRHS = []

# rhsAndlhs() will generate list of LHS and RHS


def rhsAndlhs():
    x = 0
    while x < p:
        LHS = (x * x) % p
        listLHS.append(LHS)
        RHS = (x * x * x + a * x + b) % p
        listRHS.append(RHS)
        x = x + 1

    print("LHS", listLHS)
    print("RHS", listRHS)

#affinePoints() will generate all affine points


def affinePoints():
    point = 0
    i = 0
    for n in listRHS:
        r = 0
        for n2 in listLHS:
            if n != n2:
                r = r + 1
            else:
                r2 = r
                r = r + 1
                point = r2
                print(f"({i}, {point})")
        i = i + 1

rhsAndlhs()
affinePoints()

def check(x2g,y2g):

    if x2g==xg:
        return 0
    else:
        return 1

xg = int(input("Enter Generator Point(xg):"))
yg = int(input("Enter Generator Point(yg):"))

s1 = (3*pow(xg,2)+a)%p
s2 = (2*yg)%p

s= ((s1)%p * (pow(s2, p-2))%p)%p
x2g = (pow(s, 2) - 2 * xg) % p
y2g = (s*(xg - x2g) - yg) % p

print(f"2G{x2g},{y2g}")

x2 = x2g
y2 = y2g
x1 = xg
y1 = yg

n = 3

while (x2!=0 or y2!=0) and check(x2,y2)==1:

    s1 = (y2 - y1) % p
    s2 = (x2 - x1) % p
    s = (s1 * pow(s2, p - 2)) % p
    x3g = (pow(s, 2) - x1 - x2) % p
    y3g = (s * ((x1 - x3g) % p) - y1) % p
    print(f"{n}G({x3g},{y3g}) ")

    n = n+1

    x2 = x3g
    y2= y3g
print(f"{n}G(0)")
print(f"Value of N:{n}")
