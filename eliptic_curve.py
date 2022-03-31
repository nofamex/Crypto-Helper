import pandas as pd

e = int(input("E: "))
a = int(input("a: "))
b = int(input("b: "))

def point_finder(y, y_arr):
    ans = []
    for i in range(len(y_arr)):
        if y_arr[i] == y:
            ans.append(i)
    return ans


def elyptic(e, a, b):
    if(4*(a**3) + 27*(b**2) == 0):
        print("Singular")
        return
    
    y_data = {"y": [], "y^2 mod 13": []}
    for i in range(e):
        y_data["y"].append(i)
        y_data["y^2 mod 13"].append((i**2)%13)
    
    df_y = pd.DataFrame(data=y_data)
    print(df_y)

    x_data = {"x": [], "equal": [], "y": [], "points": []}
    for i in range(e):
        x_data["x"].append(i)
        eq = (i**3 + a*i + b) % e
        x_data["equal"].append(eq)
        points = point_finder(eq, y_data["y^2 mod 13"])
        if len(points) == 0:
            x_data["y"].append("-")
            x_data["points"].append("-")
        else:
            x_data["y"].append(points)
            xy_points = [(i, x) for x in points]
            x_data["points"].append(xy_points)
    
    df_x = pd.DataFrame(data=x_data)
    print(df_x)
    return

elyptic(e, a, b) 