import random
import numpy as np
from matplotlib import pyplot as plt

marks = []
n=100
print("List of Student's Marks: ")
for i in range(n):
    marks.append(random.randint(1, 10))
print(marks) 

plt.hist(marks, bins=10)
plt.show() 