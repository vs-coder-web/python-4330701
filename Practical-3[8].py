import math
pi=3.14
height = int(input("Please enter the height of the ladder: "))
deg = int(input("Please enter the angle of the ladder in degrees: "))
rad = (pi/180) * deg
leng = height/(math.sin(rad))
print("The length of the ladder must be: ", leng)
