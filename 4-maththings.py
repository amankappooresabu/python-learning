import math

#Exercises

r = float(input('Enter the radius of the circle :'))
c = 2 * math.pi * r
print(round(c,2))

a = math.pi * pow(r,2)
print(round(a,2))

side1 = float(input('Enter first side :'))
side2 = float(input('Enter second side :'))

side3 = math.sqrt(pow(side1,2) + pow(side2,2))
print(int(side3))
