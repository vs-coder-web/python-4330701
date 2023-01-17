n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n+1,2):
    sum=sum+(i/(i+2))
    print('sum=',sum)
print("The sum of series is: ",sum)