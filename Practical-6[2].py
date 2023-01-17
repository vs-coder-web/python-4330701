n=int(input('How many Elements do you need: '))
lst=[]
for i in range(1,n+1):
    lst.append(int(input('Enter Elements: ')))
print(lst)
pos=0
neg=0
zer=0
odd=0
even=0
sum1=0
for i in lst:
    sum1=sum1+i
    avg=sum1/n
    if i%2==0:
        even+=1
    else:
        odd+=1
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zer+=1
print('Total even numbers are: ',even)
print('Total odd numbers are: ',odd)
print('Total positive numbers are: ',pos)
print('Total negative numbers are: ',neg)
print('Total zero numbers are: ',zer)
print('Average of all numbers are: ',avg)