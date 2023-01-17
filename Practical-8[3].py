def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

# Take Input from the User
nterms = int(input("How many terms do you need: "))

# Check if the number of terms are valid
if nterms <= 0:
    print("Please enter a Positive Integer")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))
        