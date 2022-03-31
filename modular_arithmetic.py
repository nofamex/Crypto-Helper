import pandas as pd

print("Mul: Multiplicataion\nAdd: Addition\nSub: Substraction")
art: str = input("operator: ")
n: int = int(input("modulo: "))

def operator(a: str, x: int, y:int):
    if (a == "Mul"):
        return (x*y)%n
    if (a == "Add"):
        return (x+y)%n
    if (a == "Sub"):
        return (x-y)%n

data = {}

for i in range(n):
    data[str(i)] = []
    for j in range(n):
        data[str(i)].append(operator(art, i, j))

df = pd.DataFrame(data=data)
print(df)