text_file = open("prac104.txt", "x")
text_file.write("The quick brown fox jumps over the lazy dog.")
text_file.write("The lazy dog was jumping over the quick brown fox.")
text_file.close()

import string

def main():
    
    file = input("Enter the name of original file: ")
    infile = open(file, 'r')
    
    otherfile = input("Enter the name of file to write to: ")
    outfile = open(otherfile, 'w')
    
    for line in infile:
        words = line.split()
        for word in words:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 4:
                if "." in word:
                    word = "****."
                elif "," in word:
                    word = "****,"
                elif "?" in word:
                    word = "****?"
                elif "!" in word:
                    word = "****!"
                else:
                    word = "****"
            print(word + " ", file = outfile, end = " ")
    infile.close()
    outfile.close()
    
if __name__ == '__main__':
    main()
    
print("The Modified File: ")
text_file = open("pracaz.txt", "r")
print(text_file.read())