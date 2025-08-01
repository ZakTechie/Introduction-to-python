# name = "Ahmed"
# # String interpolation
# greeting = f"hello, {name}"
# print(greeting.upper())

# int , float , complex
# a = 5 
# b = 3.14 
# c = 1 + 4j 

# print(int(c.imag))
# print(int(c.real))

# fruits = ["apple" , "banana" , "cherry"] # list
# # fruits[1] = "orange"
# fruits.append("orange")
# print(fruits)

# dimensions:tuple = (1920 , 1080)
# dimensions[1] = 78 # Error 
# print(dimensions[1])

# numbers = range(1 , 5 ) #
# print(tuple(numbers))

# person:dict = {
#     "name" : "Ahmed" , 
#     "age" : 30 , 
#     "city" : "cairo"
#     }
# print(person["age"] + 1)
# # print(person["job"])
# print(person.get("age" , "Not here")) # safe to get value

# colors:set = {"red" , "blue" , "green" }
# colors.add("yellow")
# print(colors)

# frozen = frozenset([1 , 2 , 3])
# frozen.add(4)


# is_valid = True 
# if is_valid:
#     print("Proceed")

# text = input("Enter any word")
# if bool(text):
#     print("You entered data")
# else:
#     print("not entered any data")


# b:bytes = b"Aello" # bytes (immutable)
# ba:bytearray = bytearray(b)
# ba[0] = 72 
# print(ba)

# mv = memoryview(b)
# mv[0] = 72 # Maker error cannot modify (read-only memory)

# ===================================================================
# String Methods

# description = '''this is for test
#         today is very hot
# kfjdkfd
# kldkfldjjkf
# gs;j'''

# print(description)

# 1- slice
# b = "Hello, world"
# print(b[ ::-1 ]) 

# num = input("Enter your number: ")
# print(num[::-1])

# 2- Repeat 
# num = int(input("Enter your #border"))
# print("=" * num)
