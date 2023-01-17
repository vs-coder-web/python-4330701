j=1
for i in range(33,127):
    if j%5==0:
        print(chr(i))
    else:
        print(chr(i),end='   ')
    j=j+1
print()