# EMI Calculator program in Python
def emi_calculator(p, r, t):
    r = r / (12 * 100)
    t = t * 12
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    return emi

# Driver Code
principal = int(input("Enter The Principal Amount: "))
rate = int(input("Enter The Rate of Interest: "))
time = int(input("Enter The Time Period: "))
emi = emi_calculator(principal, rate, time)
print("The Monthly EMI is:: ", emi)