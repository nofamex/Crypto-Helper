n: int = int(input("n: "))
power: int = int(input("pow: "))
mod: int = int(input("mod: "))

def gcd(a:int, b:int):
    if b == 0:
        return a
    return gcd(b, a%b)

def euler(n: int):
    ans = []
    for i in range(n):
        if gcd(i, n) == 1:
            ans.append(i)
    return len(ans)

eul = euler(mod)
res = power%eul
ans = (n**res)%mod
print(ans)