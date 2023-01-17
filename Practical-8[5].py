# Recursive function to return GCD of two numbers
def gcd(a, b):
    
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
    
    # Base Case
    if (a == b):
        return a
    
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

# Driver Program
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
if(gcd(a, b)):
    print("GCD of", a , "and", b , "is: ", gcd(a, b))
else:
    print("Not Found")