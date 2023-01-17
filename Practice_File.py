# Performing List Operations

# Printing The List
print('My Student List: ')
student = [22, 'Vraj', 'AB', 63, 70]
print(student)

# Add Items To The List

print('\nAdding Items To The List: ')
student.insert(3, 46) #At Indexed Position
student.insert(4, 72)
print(student)
student.append(85) #At The End Of List
print(student)

#Remove Items From The List

print('\nRemoving Items From The List: ')
student.remove(46) #Removes Inserted Item
print(student)
del student[4] #Removes Item Through Index Number
print(student)
student.pop() #Removes Last Item From The List
print(student)

# Getting The Length Of The List
print('\nThe Length of the Student List is: ', len(student))

# Accessing List Elements Through Index
print('\nAccessing List Elements Through Index: ')
print('student [0] = ', student[0])
print('student [2] = ', student[2])
print('student [4] = ', student[4])

#Sorting The List
print('Sorting The List:\n')
sortlist = [23, 83, 72, 92, 29, 46, 17, 39, 63, 50]
print('\nThe Unsorted List: ', sortlist)
sortlist.sort() #Function To Sort The List
print('\nThe Sorted List: ', sortlist)
sortlist.sort(reverse=True) #Sorting In Descending Order
print('\nThe Sorted List In Descending Order: ', sortlist)

#Reversing The List
sortlist = [23, 83, 72, 92, 29, 46, 17, 39, 63, 50]
print('\nOriginal List: ', sortlist)
sortlist.reverse()
print('\nReversed List: ', sortlist)


'''

2. Number Triangle Pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end= " ")
    print(" ")



1. Remove duplicates from the list

n = int(input('How many elements do you require: '))
list1 = []
for i in range(1, n+1):
    list1.append(int(input('Enter The ELements: ')))
print('Your Elements: ', list1)
d = []
for i in list1:
    if i not in d:
        d.append(i)
print('Elements after removing Duplicates: ', d)
'''

