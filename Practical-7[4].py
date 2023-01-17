temperature={}
temperature['Sunday']=int(input("Enter temperature for Sunday: "))
temperature['Monday']=int(input("Enter temperature for Monday: "))
temperature['Tuesday']=int(input("Enter temperature for Tuesday: "))
temperature['Wednesday']=int(input("Enter temperature for Wednesday: "))
temperature['Thursday']=int(input("Enter temperature for Thursday: "))
temperature['Friday']=int(input("Enter temperature for Friday: "))
temperature['Saturday']=int(input("Enter temperature for Saturday: "))
for i,j in temperature.items():
 if j>=40 and j<=50:
    print(i)
