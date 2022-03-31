from math import floor

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

g = int(input("find until xG: "))
gx = int(input("gx: "))
gy = int(input("gy: "))
a = int(input("a: "))
b = int(input("b: "))
p = int(input("p: "))

data = [(gx, gy)]

for i in range(2, g+1):
    curr = data[-1]
    Xp = curr[0]
    Yp = curr[-1]
    Xq = gx
    Yq = gy

    if (i%2 == 0):
        curr = data[floor(i/2) - 1]
        Xp = curr[0]
        Yp = curr[-1]
        Xq = Xp
        Yq = Yp
        print(f"{i}G = {floor(i/2)}G+{floor(i/2)}G = {curr} + {curr}")
    else:
        print(f"{i}G = {i-1}G+G = {curr} + {(gx,gy)}")
    print(f"Xp = {Xp}, Yp = {Yp}")
    print(f"Xq = {Xq}, Yq = {Yq}")

    lam = 0
    if (i%2 == 0):
        up = 3*(Xp ** 2)+a
        down = 2*Yp
        lam = (up * modInverse(down, p)) % p
        if down <= 0:
            lam = (up * (down % p)) % p
        print(f"lambda = 3({Xp})^2 + {a} / 2({Yp}) mod {p}")
        print(f"={up} / {down} mod {p}")
        print(f"={lam}\n")
    else:
        up = Yq -Yp
        down = Xq-Xp
        lam = (up * modInverse(down, p)) % p
        if down <= 0:
            lam = (up * (down % p)) % p
        print(f"lambda = ({up}/{down}) mod {p}")
        print(f"={lam}\n")


    Xr = floor((lam**2 - Xp - Xq) % p)
    print(f"Xr = (lambda^2 - Xp - Xq) mod p")
    print(f"=({lam**2} - {Xp} - {Xq}) mod {p}")
    print(f"={Xr}\n")

    Yr = floor((lam*(Xp-Xr)-Yp) % p)
    print(f"Yr = (lambda(Xp-Xr)-Yp) mod p")
    print(f"=({lam}({Xr} - {Xp})-{Yp}) mod {p}")
    print(f"={Yr}\n")

    nG = (Xr, Yr)
    data.append(nG)
    print(f"Maka, {i}G = {nG}\n")

# Somehow buggy kalo pembaginya 0 eg: 5/0 mod 13
# jadi ntar di cek lagi aja kalo ada pembagi 0 tehe
# kalo mau aman jangan pake sih rada buggy
