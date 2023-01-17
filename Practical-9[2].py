import random
print("Welcome To Rock-Paper-Scissor Game !!!")
print("Choices In Game: \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissor \n")

while True:
 
	# take the input from user
	choice = int(input("Enter Your Choice: "))

	# looping until user enter invalid input
	while choice > 3 or choice < 1:
		choice = int(input("Enter Valid Input: "))

	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'Paper'
	else:
		choice_name = 'Scissor'

	# print user choice
	print("User Choice is: " + choice_name)
	comp_choice = random.randint(1, 3)
 
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'Paper'
	else:
		comp_choice_name = 'Scissor'

	print("Computer's Choice is: " + comp_choice_name)

	print(choice_name + " V/S " + comp_choice_name)

	if choice_name == comp_choice:
		result = Draw
		print("Draw", end="")
		

	# condition for winning
		if((choice == 1 and comp_choice == 2) or
		(choice == 2 and comp_choice == 1)):
			print("Paper Wins ", end="")
			result = "paper"
		elif((choice == 1 and comp_choice == 3) or
				(choice == 3 and comp_choice == 1)):
			print("Rock Wins ", end="")
			result = "Rock"
		else:
			print("Scissor Wins", end="")
			result = "Scissor"

	# Printing either user or computer wins or draw
	if result == Draw:
		print("Its a Tie !!!")
	if result == choice_name:
		print("User Wins !!!")
	else:
		print("Computer Wins !!!")
