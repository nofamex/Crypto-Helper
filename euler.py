n: int = int(input("n: "))

ans = []

def gcd(a:int, b:int):
    if b == 0:
        return a
    return gcd(b, a%b)

for i in range(n):
    if gcd(i, n) == 1:
        ans.append(i)

# Uncomment line below to see all element in reduced set
# print(ans)

print(f"euler totient = {len(ans)}")