#Create a dictionary.
person={'name':'Vraj','age':18,'salary':26000}
print(type(person))
#Print dictionary items.
print("Name:",person['name'])
print("Age:",person['age'])
print("salary:",person['salary'])
#Add/remove key-value pair in/from a dictionary.
edict={}
print('Empty Dictionary')
print(edict)
edict[0]="Vraj"
edict[1]="Soni"
print(edict)
del edict[1]
print(edict)
'''del edict
print(edict)'''
#Check whether a key exists in a dictionary.
key1=input('Enter Key Name: ')
if key1 in person.keys():
 print('Key is in dictionary')
else:
 print('Key is not in dictionary')
#Iterate through a dictionary.
employee={'Name':'Vraj','Age':18,'Salary':26000}
for x in employee:
 print(x)
for x in employee.values():
 print(x)
for x in employee.items():
 print(x)
for x,y in employee.items():
 print(x,y)
#Concatenate multiple dictionaries.
person.update(edict)
print(person)
