import json

data = '{"name" : "Karim" , "age" : 65 , "city" : "USA"}'

# Convert from JSON to python 
# loads
# dict1 = json.loads(data)
# print(dict1["name"])


# Convert from python to JSON

# dumps()

# dict1 = {
#     "name" : "john" , 
#     "age" : 55 , 
#     "city" : "cairo"
# }

# data = json.dumps(dict1)
# print(data["name"])


# data = json.dumps(("apple" , "banana"))
# data = json.dumps(True)
# data = json.dumps(None)
# print(data)



a = {
    "name" : "gamal" , 
    "age" : 55 , 
    "married" : True , 
    "children" : ("Ann" , "billy"),
    "pets" : None , 
    "cars" : [
        {"model" : "BMW" , "color" : "red"},
        {"model" : "Ford" , "color" : "white"}
    ]
}


print(json.dumps(a , indent= 5 , separators=("." , " = ") , sort_keys= True))