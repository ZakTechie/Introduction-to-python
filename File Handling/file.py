# open()

# frist_parameter ==> filename
# second_parameter ==> mode 

# Mode:
# "r" ===> reading
# "a" ==> append 
# "w" ==> overwrite , create file if it doesn't exist 
# "x" ==> create file , return error if the file exists 
# "t" ==> Text == Default value 
# "b" ==> binary mode (images)


# Methods 
# read()
# readline()
# readlines()
# seek()
# f = open("../../demo.txt" , "rt")
# print(f.read())
# f.close()

# with open("../../demo.txt") as f:
#     f.seek(2 , 0)
#     print(f.read(4))


# with open("demo.txt" , "a") as f:
#     f.write("now the file has more content! Zack")
#     for i in range(4):
#         f.write("\n")
#         f.write("now the file has more content! Zack")

# with open("demo.txt")as f:
#     print(f.readline())
 

# if os.path.exists("./demo.txt"):
#     os.remove("./demo.txt")
# else:
#     print("the file does not exists")


# to run any program 
# import os 
# os.startfile("test.mp3")

