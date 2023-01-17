 # Defining Function To Convert String into Numeric Value
def name_value(name):
    name = name.lower()
    value = 0
    for char in name:
        value += ord(char) - 96
    return value

name = input("Enter Your Name: ")
print("Value of Your Name: %d" % name_value(name))
