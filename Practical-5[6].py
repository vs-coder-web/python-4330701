for i in range(1,10000):
    sum = 0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print("Perfect Numbers: ",i)
