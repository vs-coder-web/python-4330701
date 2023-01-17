import math
a,b,c = map(int,input('Enter Values: ').split())
x = int((-b + math.sqrt(b**2-4*a*c))/2*a)
y = int((-b - math.sqrt(b**2-4*a*c))/2*a)
print("x1=",x," , ","x2=",y)