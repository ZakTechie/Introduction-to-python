# # # # try
# # # # except 
# # # # else
# # # # finally 

# # # try:
# # #     print(a)
# # # # except IndexError:
# # # #     print("you use variable not declare")
# # # # except NameError:
# # # #     print("variable not defined")
# # # except:
# # #     print("error")
# # # else:
# # #     print("No thing error")
# # # finally:
# # #     print("The end")

# # # # # print(a)

# # # # print("Hello")


# # try:
# #     f = open("demofile.txt" )
# #     try:
# #         f.write("Lorem")
# #     except:
# #         print("something wrong in writing file")
# #     finally:
# #         f.close()
# # except:
# #     print("Some thing wrong in open file")


# # a = -1 
# # if a < 0 :
# #     raise Exception("Sorry , no numbers allow below zero")
# try:
#     a = "Hello"
#     if not type(a) is int:
#         raise TypeError()
# except TypeError:
#     print("Only integers are allowed")