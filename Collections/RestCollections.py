# # thistuple = ("apple" , "banana" , "cherry")
# # print(thistuple[0])
# # print(len(thistuple))
# # tupl1 =("abc" , 34 , True)
# # print(type(tupl1))

# # print(thistuple[-1::-1])
# # if("apple" in thistuple):
# #     print("Found")

# # update tuple 
# # y = list(thistuple)
# # y[0] = "orange"
# # thistuple = tuple(y)
# # print(thistuple)

# # tup1 = ("apple" , "banana" , "cherry")
# # tup2 = ("orange",)
# # tup1 += tup2
# # print(tup1)

# # upack tuple
# # fruits = ("apple" , "banana" , "cherry")
# # (green , yellow , red) = fruits
# # print(green)
# # print(yellow)
# # print(red)

# names = ("Ahmed" , "Ali" , "Gamal" , "Mahmoud")
# # (a , _ , b , _)= names

# # # print(a , b)
# # # print(names[0] , names[-1])
# # (a , *b , c) = names 
# # print(b)

# # for n in range(len(names)):
# #     print(names[n])
# names1 = ("Dina" , "Eman")
# n = names + names1
# print(n * 3)

# # print("hello" * 3)


# Tuple Methods
# names = ("Ahmed" , "Ali" , "Gamal" , "Mahmoud")
# print(names.index("Ahmed"))
# ===========================================================
# Set
myset = {"apple" , "banana" , "cherry" , "apple"}
# print(myset)

# myset = {"apple" , 3 , True}
# print(len(myset))

# for n in myset:
#     print(n)

# m = list(myset)
# print(m)

# myset.add("orange")
# print(myset)

# myset2 = ["mango" , "papaya"]
# myset.update(myset2)
# print(myset)

# myset.remove("orange")
# print(myset)

# myset.discard("orange")
# print(myset)

# m = myset.pop()
# print(m)
# print(myset)

# myset.clear()
# print(myset)

# del myset
# print(myset)


# for n in myset : 
#     print(n)

# union() 
# intersection()
# difference()
# symmetric_difference

set1 = {"a" , "B" , "C"}
set2 = {1 ,3 , 4}
set3 = {True , False} 
set4  = {5.5}
tup = (1 , 2 , 3)
# set1.update(set2)
# print(set1)
# union()
# set3 = set1 | (set2)
# print(set3)

# set5 = set1.union(set2 , set3 , set4)
# print(set1.union(set2 , set3 , set4))
# z = set1.union(tup)
# print(z)

# set1 = {"apple" , "banana" , "cherry" , 1 , 0}
# set2 = {"google" , "microsoft", False , "apple" , True}

# set1.difference_update(set2)
# set1 -= set2
# print(set1)
# # set3 = set1.intersection(set2)
# # set3 = set1 & set2
# # print(set3)
# # set1.intersection_update(set2)
# # print(set1)
# # set3 = set1.difference(set2)
# # set3 = set1 - set2
# # print(set3)

# # set1.difference_update(set2)
# # print(set1)

# # set3 = set1.symmetric_difference(set2)
# # set3 = set1 ^ set2
# # print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)

# set Methods 
# add()
# clear()
# copy()
# difference() - 
# difference_update() -=
# discard()
# intersection() &
# intersection_update &=
# isdisjoint()
# issubset() <=
# issuperset() >=
# pop()
# remove()
# symmetric_difference
# symmetric_difference_update
# union()
# update()

# x = {1 , 2 , 3}
# y = {1 , 2 , 3, 4, 5 ,6}
# print(y.issuperset(x))

