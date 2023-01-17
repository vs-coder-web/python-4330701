# Enter The Date in DD/MM/YYYY Format
date = input("Enter Date in (DD/MM/YYYY) Format: ")

date = date.split("/")

# Printing Date in MM-DD-YYYY Format

print("Date in (MM-DD-YYYY) Format: %s-%s-%s" % (date[1], date[0], date[2]))