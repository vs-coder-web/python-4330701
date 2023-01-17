from itertools import combinations
numbers=[]
for i in range (1,10):
 j=int(input('Enter No: '))
 numbers.append(j)
c=combinations(numbers,2)
for e in c:
 print(e)