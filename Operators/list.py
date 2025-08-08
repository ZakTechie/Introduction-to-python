# mylist= ["apple" , True , 3]
# print(type(mylist))

# theList = list(("apple" , "banana" , "cherry"))
# print(theList)

# mylist[0] = False 
# # print(mylist)
# mylist[0:3] = ["Ford" , "BMW" , True]
# print(mylist)

# # mylist.insert(1 , "Watermelon")
# mylist.append("watermelon1")
# print(mylist)

# Add Items : append() , insert() , extend()
# secondList = ("mango" , "papaya")
# mylist.extend(secondList)
# print(mylist)

# Remove Items : remove() , pop() , del , clear()
# mylist= ["apple" , True , 3]
# mylist.remove("apple")
# mylist.pop(0)
# del mylist[0]
# mylist.clear()
# print(mylist)

# for i in range(len(mylist)):
#     print(mylist[i])
# i = 0 
# while(i < len(mylist)):
#     print(mylist[i])
#     i +=1

# [print(x) for x in mylist]

# [print(z) for z in mylist]
# mylist = ["orange" , "apple" , "banana"] 
# # mylist.sort(key = str , reverse=True)
# # mylist.reverse()
# NewList = mylist.copy()
# print(NewList)


list1 = ["a" , "b" ,"c"]
list2 = [1 , 3, 4]
# list3 = list1 + list2 
# print(list3)

# for i in list2:
#     list1.append(i)

# print(list1)

# list1.extend(list2)
# print(list1)


my = ["apple" , "apple" , "orange"]
# print(my.count("apple"))
print(my.index("apple"))