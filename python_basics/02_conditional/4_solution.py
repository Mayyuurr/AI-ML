fruit =input("Fruit:-")

color=input("color of fruit:- ")

if fruit=="Banana":
    if color=="Green":
        print("unripe")
    elif color=="Yellow":
        print("Ripe")
    elif color=="Brown":
        print("overripe")
else:
    print("Unknown Fruit, Data unavalibale")