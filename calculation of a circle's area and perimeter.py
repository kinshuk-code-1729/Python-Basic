import math as m
radius=float(input("Enter radius of the circle:"))
print("1. Calculate Area")
print("2. Calculate Circumference")
choice=int(input("Enter your choice(1 or 2):"))
if choice==1:
    area=m.pi*radius*radius
    print("Area of circle with radius",radius,'is',area)
elif choice==2:
    perm=2*m.pi*radius
    print("Circumference of circle with radius",radius,'is',perm)
else :
    print("Invalid Operation !!!!!")
