#Create two different sets with the data.
Days=set(['mon','tue','wed'])
Days2=set(['wed','tue','thu'])
# Print set items.
for d in Days:
 print(d)
# Add/remove items in/from a set.
Days.add('saturday')
print(Days)
Days.discard('mon')
print(Days)
# Perform operations on sets: union, intersection, difference, symmetric difference, check subset of another set.
#union
print("days set",Days)
print("days2 set",Days2)
print("union")
print(Days|Days2)
print(Days.union(Days2))
#intersection
print("intersection")
print(Days&Days2)
print(Days.intersection(Days2))
#difference
print("difference")
print(Days-Days2)
print(Days.difference(Days2))
#symmetric difference
print("Symmetric Difference")
print(Days^Days2)
#check subset
set1=([1,2,3,4,5,6])
set2=([1,2,3])
set3=([1,2])
if(set3<set2):
 print("set3 is subset of set2")
else:
 print("set3 is superset of set2")