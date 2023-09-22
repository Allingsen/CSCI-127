import math
import random

#Sets a and b as random numbers (int and float)
a = random.randint(1,10)
b = random.uniform(0,10)
b = round(b, 2)
print("a is ", a)
print("b is ", b)

#Sets c as a user inputted float
c = input("Please enter a value for c:")
c = float(c)
c = abs(c)
#Cone is used as the mathmatic version of c
cone = math.copysign(c, -0.0)
print("c is ", cone)

print(str(a) + "x^2 + " + str(b) + "x - " + str(c) + " = 0")

#Gets the X values
xone = (-b + (math.sqrt((b**2)-(4*a*cone))))/(2*a)
xtwo = (-b - (math.sqrt((b**2)-(4*a*cone))))/(2*a)
print("x is ", xone, "and", xtwo)
