n=int(input('How many elements do you require for List: '))
lst=[]
for i in range(1,n+1):
    lst.append(int(input('Enter Elements: ')))
print(lst)
c=[]
for i in lst:
    if i not in c:
        c.append(i)
print(c)
