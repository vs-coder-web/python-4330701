p = int(input('Enter The Principle Amount: '))
n = int(input('Enter No. of Years: '))
r = int(input('Enter Rate of Interest: '))
SI = (p * n * r) / 100
print('Simple Interest = ', SI)
t = int(input('Enter The Time Period: '))
CI = p * pow(1 + (r / 100 * n), (n * t))
print('Compound Interest = ', CI)