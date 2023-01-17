fname = input("Enter file name: ")
l = input("Enter the letter to search: ")
k = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter == l):
                    k = k+1

print("Occurrence of the letter: ", k)