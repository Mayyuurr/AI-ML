distance=int(input("distance to travel:- "))

if distance<3:
    transport="Walk"
elif distance<16:
    transport="Bike"
elif distance>15:
    transport="car"

print(transport)