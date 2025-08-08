# mylist = ["apple"  , "orange" , "apple"]
# name = input("Enter name of fruit: ")
# li = []
# m = input("Enter name of fruit: ")
# print(name is m)
# for n in range(len(mylist)):
#     if(name == mylist[n]):
#         li.append(n)
#     # print(mylist[n])

# print("your word is " , name , "ocurrences in mylist : ",  li)

# identity
x= ["apple" , "banana"]
# y = ["apple" , "banana"]
y = x
z = x
print(z) 
print(x is z) # True
print(x is y ) # True
print(x == y ) # True