# thisdict = {
#     "brand" : "Ford" , 
#     "model" : "Mustang" , 
#     "year" : 1964 ,
#     "status" : True , 
#     "year" : 2005 , 
#     "colors" : ["red" , "white" , "blue"], 
#     "person1" : {
#         "name" : "Ahmed" ,
#         "age" : 18 
#     }
# }

# for n in thisdict.keys():
#     if n == "person1":
#         for y  , v in thisdict[n].items():
#             print(y , v , sep= "\t\t")
# # print(thisdict["person1"]["name"])
# # print(thisdict["year"])
# # print(thisdict["colors"][0])
# # print(type(thisdict))

# thisdict = dict(brand = "Ford" , model = "Mustang" , year = 1967 , colors=["red" , "white" , "blue"])
# # print(thisdict)

# # thisdict["year"] = 2000 
# # print(thisdict["year"])

# # update()
# # thisdict.update({"year" : 2020})
# # print(thisdict)

# # thisdict["address"] = "Egypt" 
# # print(thisdict)
# # thisdict.update({"address" : "Egypt"})
# # print(thisdict)

# # pop() ==> remove the item with specified key name 
# # thisdict.pop("year")
# # print(thisdict)

# # popitem() ==> remove last inserted item 
# # thisdict.popitem()
# # print(thisdict)

# # del
# # del thisdict["brand"] 
# # print(thisdict)

# # clear()
# # thisdict.clear()
# # print(thisdict)


# # loop Dictionary
# # for n in thisdict:
# #     print(thisdict[n])

# # for n in thisdict.values():
# #     print(n)

# # for n in thisdict.keys():
# #     print(n)


# # for n , y in thisdict.items():
# #     print(n , y , sep="\t")


# # dict2 = dict(thisdict)
# # thisdict["brand"] = "BMW"
# # print(dict2) 

# # thisdict["brand"] = "BMW"
# # dict2 = thisdict.copy()
# # print(dict2)


thisdict = {
    "brand" : "Ford" , 
    "model" : "Mustang" , 
    "year" : 1964 ,
    "status" : True , 
    "year" : 2005 , 
    "colors" : ["red" , "white" , "blue"], 
    "person1" : {
        "name" : "Ahmed" ,
        "age" : 18 
    }
}


# Dictionary Methods :
# clear()
# copy()
# fromkeys() ==> return dictionary with specified keys and specified value 
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault() ==> 
# print(thisdict.get("brand"))
# thisdict.setdefault("brand" , "BMW")
# print(thisdict)
# update()
# values()

# # Task: 
# zip()
# x = ("key1" , "key2" , "key3")
# # # x = "key1"
# y = (1 , 10 , 40)

# # thisdict = dict.fromkeys(x , y )
# # print(thisdict)

# # ==========================================

# thisdict = dict.fromkeys(x , y)
# print(thisdict)

