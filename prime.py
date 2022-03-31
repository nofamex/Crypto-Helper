n: int = int(input("n: "))

divider = []

for i in range(1, n+1):
    if(n%i == 0):
        divider.append(i)

if len(divider) == 2:
    print("Prime")
else:
    print("not prime")