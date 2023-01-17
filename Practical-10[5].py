# Taking HEX Value From User
hex = input("Enter The HEX Code: ").lstrip('#')

# Printing RGB Value From HEX Value
print("\nValues in RGB Are: \n")
print("(Red, Green, Blue) = ", tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))
