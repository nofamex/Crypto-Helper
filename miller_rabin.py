from math import floor


n: int = int(input("n: "))
a: int = int(input("a: "))

do = True
k = 1
q = 0

while(do):
    if((n-1)%(2**k) == 0):
        q = floor((n-1)/(2**k))
        k += 1
    else:
        do = False
        k -= 1

print(f"k = {k}, q = {q}")

def miller(a, k ,q):
    if ((a**q)%n == 1):
        return "inconclusive"
    else:
        for i in range(1, k):
            if((a**((2**i)*q))%n == n-1):
                print(f"i = {i}")
                return "inconclusive"
    return "composite"

print(miller(a, k, q))