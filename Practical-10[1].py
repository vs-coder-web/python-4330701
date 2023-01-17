# Function to check whether the String is Palindrome or not

s = str(input("Enter The String: "))

def Palindrome(s):
    return s == s[::-1]

# Driver Code

string = Palindrome(s)

if string:
    print("The String is Palindrome")
else:
    print("The String is Not Palindrome")