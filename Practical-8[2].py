#Removing Duplicate elements from the List
lst = [7, 2, 12, 7, 4, 8, 5, 2, 6, 4]
print("Original List: ", lst)
res = [*set(lst)]
print("List after removing Duplicate Elements: ", res)