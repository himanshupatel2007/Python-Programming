import math 
a = float(input("Enter the side [Base] : "))
b = float(input("Enter the side [Perpendicular] : "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Hypoteneus : {round(c,2)}")