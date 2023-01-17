# Program to Perform Operations on Files

# Creating a Text File and Write a String to it
text_file = open("file01.txt", "x")
text_file.write("I am Vraj Soni. ")
text_file.write("I study at KJ Polyechnic. ")
text_file.write("My Department is Computer Engineering. ")
text_file.close()

# Read an entire Text File
print("Read The File: ")
text_file = open("file01.txt", "r")
print(text_file.read())

# Read a Text File Line By Line
print("\nRead The File Line By Line: ")
text_file = open("file01.txt", "r")
print(text_file.readlines())

# Writing String to a File
print("\nWriting String to a File: ")
text_file = open("file01.txt", "w")
text_file.write("Currently I am in 2nd Year. ")
text_file = open("file01.txt", "r")
print(text_file.read())
text_file.close()

# Writing List of Strings to a File
text_file = open("file01.txt", "w")
print("\nWriting List of String to a File: ")
text_file.write("I am learning Python Language.")
text_file.write("This is a File Operation.")
text_file.write("The list of strings are added to file.")
text_file = open("file01.txt", "r")
print(text_file.read())
text_file.close()

# Count the number of lines & words in a file
file = open('file01.txt')

lines = 0
words = 0

for line in file:
    lines += 1
    words += len(line.split())
    
print("Number of Words in File: ", lines)
print("Number of Lines in File: ", words)
