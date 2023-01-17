#Create a tuple with different data types.
vraj=(10,20,30,40,50)
print(vraj)

#Print tuple items.
for i in vraj:
 print(i)

#Convert tuple into a list.

 lst = list(vraj)
#print list
print(lst)

print(type(lst))

#Remove data items from a list.

lst.remove(50)
print(lst)

#Convert list into a tuple.

tpl=tuple(lst)

print(type(tpl))

#Print tuple items.
print(tpl)