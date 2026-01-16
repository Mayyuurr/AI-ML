import math

def area_circle(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius

    return area,circumference

a,c=area_circle(7)
print("area: ",round(a,3), "circumference: ", round(c,3))
