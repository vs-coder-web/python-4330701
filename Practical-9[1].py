import numpy as np

lst = []
n = int(input("Enter Number of Elements You Need: "))
for i in range(0, n):
    nums = int(input("Enter Your Elements: "))
    lst.append(nums)
print("Your List is: ", nums)

nums = np.arange(n)
mean = np.average(nums)
print("Mean: ", mean) 
deviation = np.sqrt(np.mean((nums - np.mean(nums)) ** 2))
print("Standard Deviation: ", deviation)