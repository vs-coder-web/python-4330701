# Python3 code to demonstrate
# Shuffle a List
# Using random.shuffle()

import random

# Initializing List
test_list = [2, 3, 6, 8, 11, 5]

#Printing Original List
print("Original List: " + str (test_list))

#Shuffling the List using random.shuffle()
random.shuffle(test_list)

#Printing Shuffled List
print("Shuffled List: " + str(test_list))