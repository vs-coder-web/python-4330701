text_file = open("prac1106.txt", "x")
text_file.write("The quick brown fox jumps over the lazy dog.")
text_file.close()

text_file = open("prac2106.txt", "x")
text_file.write("The lazy dog jumps over the quick brown fox.")
text_file.close()

# Select the files
file1 = "prac1106.txt"
file2 = "prac2106.txt"

# Open file in Read mode
f1 = open(file1, "r")
f2 = open(file2, "r")

# Read the file
data1 = f1.read()
data2 = f2.read()

# Remvove spaces from strings
data1 = data1.replace(" ", " ")
data1 = data1.replace(" ", " ")

# Get the length
len1 = len(data1)
len2 = len(data2)

max_len = max(len1, len2)

for i in range(max_len):
    if i < len1:
        print(data1[i], end="")
    if i < len2:
        print(data2[i], end="")
print()