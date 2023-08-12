import math
a=float(input("enter the side of the triangle:"))
b=float(input("enter the side of the triangle:"))
c=float(input("enter the side of the triangle:"))

s=(a+b+c/2)
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle",area)

