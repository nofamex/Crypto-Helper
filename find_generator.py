import pandas as pd

n: int = int(input("modulo: "))

def operator(a: str, x: int, y:int):
    if (a == "Mul"):
        return (x*y)%n
    if (a == "Add"):
        return (x+y)%n
    if (a == "Sub"):
        return (x-y)%n

data = {}

for i in range(1, n):
    data[f"a^{i}"] = []
    for j in range(1, n):
        data[f"a^{i}"].append((j**i)%n)

df = pd.DataFrame(data=data)
print(df)

gen = []
for index, row in df.iterrows():
    rows = []
    for i in range(1, n):
        rows.append(row[f"a^{i}"])
    if len(rows) == len(set(rows)):
        gen.append(index + 1)

print(gen)