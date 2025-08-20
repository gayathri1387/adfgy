list1=[i for i in range(5)]
print("Elements of list are:")
for i in range (len(list1)):
   print (list1[i])
print("length of list is",len(list1))
print("adding new item 99 using append method")
list1.append(99)
print("Elements are:",list1)
print("adding new item using insert method")
list1.insert(1,2)
print("Elements are.",list1)
print("Removing on item 1 using pop()method")
list1.pop(1)
print("Element are in list:",list1)
find=int(input("Enter the Elements to search"))
post=list1.index(find)
print("%d element found at index % d"%(find,post))



