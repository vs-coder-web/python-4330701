capitals = { "Maharashtra": "Mumbai",
 "Delhi" : "New Delhi", 
 "Gujarat" : "Gandhinagar",
 "Uttar Pradesh":"Lucknow",
 "Tamil Nadu ": "chennai",
 "Karnataka" : "Bengaluru" }
for key, value in capitals.items():
 # ask user to enter capital of state
 capital = input("Enter capital of " + key + ": ")
 
 # check if it is correct or not
 if capital==value:
    print("Correct Answer")
 else:
    print("Incorrect Answer")