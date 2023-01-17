# Take String Input From User
str1 = str(input("Enter 1st String: "))
str2 = str(input("Enter 2nd String: "))

# Convert Both The Strings into Lowercase
str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):
    
    #Sort the Strings
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    
    # If Sorted Char Arrays are same
    if (sort_str1 == sort_str2):
        print(str1 + " and " + str2 + " are Anagrams.")
    else:
        print(str1 + " and " + str2 + " are Not Anagrams.")
else:
    print(str1 + " and " + str2 + " are Not Anagrams.")

