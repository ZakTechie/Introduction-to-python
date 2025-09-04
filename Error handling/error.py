# try..except 


# result = 5 / 0 
# print(result)
# try:
#     result = 5 / 0 
#     print(result)
#     # print(z)
#     # print("Hello")
# except ZeroDivisionError:
#     print("Not Permission")
# except NameError:
#     print("this is variable is not defined")
# else:
#     print("nothing")
# finally:
#     print("End")


# try:
#     with open("demo.txt") as f :
#         print(f.read())
#         raise Exception("The file is doesn't exist")
# except:
#     print("File is doesn't exist")

# else:
#     print("Hello")



z = "Hello"

if not type(z) is int :
    raise Exception("Only integers is allowed")
 