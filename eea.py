from math import floor
import pandas as pd

b: int = int(input("b: "))
m: int = int(input("m: "))

data = {"Q": ["-"], "A1": [1], "A2": [0], "A3": [m], "B1": [0], "B2": [1], "B3": [b]}

while(data["B3"][-1] != 0 and data["B3"][-1] != 1):
    Q = floor(data["A3"][-1]/data["B3"][-1])
    A1 = data["B1"][-1]
    A2 = data["B2"][-1]
    A3 = data["B3"][-1]
    B1 = data["A1"][-1] - (Q * data["B1"][-1])
    B2 = data["A2"][-1] - (Q * data["B2"][-1])
    B3 = data["A3"][-1] - (Q * data["B3"][-1])

    data["Q"].append(Q)
    data["A1"].append(A1)
    data["A2"].append(A2)
    data["A3"].append(A3)
    data["B1"].append(B1)
    data["B2"].append(B2)
    data["B3"].append(B3)


df = pd.DataFrame(data=data)
print(df)