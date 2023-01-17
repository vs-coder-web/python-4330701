text_file = open("prac03.txt", "x")
text_file.write("I am Vraj. ")
text_file.write("My age is 18. ")
text_file.write("My roll no is 22. ")
text_file.write("My Pin Code is 390025.")
text_file.close()

fname = "prac03.txt"

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print("Numbers found: ", letter)