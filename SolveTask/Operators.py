# Arithmetic operator  Done
# Assignment operator  Done
# comparison Operator  Done
# Logical Operator    Done
# identity operator  Done
# Membership operator Done
# Bitwise operator  Done

# num1 = 3 
# num3 = 4 
# print(num1 + num3) #  7
# print(num1 - num3) # -1
# print(num1 * num3) # 12
# print(num1 / num3) # 0.75
# print(num1 % num3) # 3
# print(num1 ** 3) # 27 
# print(num1 // num3) # 0

# Assignment Operator 
# =
# +=
# -=
# *=
# /=
# **=
# //=
# &=
# |=
# ^=
# <<=
# >>=
# :=

# n = 4  
# # # n += 3  ==> n = n + 3
# # n = n - 3 
# # n -= 3
# n ^= 3 
# print(n)  
# # 100
# # 011
# # =======
# 111


# >>= Right shift operator 
# n = 3
# n >>= 2 
# #  3 / 2^2 
# print(n) 

# # <<= Left shift Operator
# n = 3 
# n <<= 3 
# # 3 * 2^3
# print(n)


# :=
# z = 3 
# print(z)

# print(z:=3)
# print(z)

# Comparison operator 
# == 
# != 
# >
# <
# >=
# <=

# Logical operator 
# and 
# not
# or

# num = int(input("Enter any number: "))
# if (num > 4 and not num < 10):
#     print("Number between 4 and 10 ")
# else:
#     print("None")

# identity operator 
# is 
# is not 
# name1= 5
# name2 = 6
# print(name1 is not name2)


# Membership operator 
# in 
# not in 

# users = ["Ahmed" , "Mohamed" , "Ali"]
# user_name = input("Enter your username: ")
# if(user_name in users):
#     print("login Success")
# else:
#     print("falied login")

# Bitwise operator
# & 
# |
# ^
# ~
# <<
# >>

# print(3+4 & 5)
# # 111 
# # 101
# # =====
# # 101


# opertor priority == precedence 
# print((6+3) - (3+5)) # 1
# print(100 + 5 * 4) # 120 

# 1- ()
# 2- **
# 3- +x -x ~x
# 4- * / // %
# 5- + - 
# 6- << >> 
# 7- &
# 8- ^
# 9- |
# 10- comparison , identity , membership 
# 11- not 
# 12- and 
# 13- or

# n = 3 
# print(100 + -(~n)) 
# 011
# 100 ==> -4
n = 4 
print((4**2) + 7 - n // 2 & n) 
#  16 + 7 - 4 // 2 & 4 
# 16 + 7 - 2 & 4
# 21 & 4 
# 16 8 4 2 1
#  1 0 1 0 1
#  0 0 1 0 0
# ===========
#  0 0 1 0 0


print(3 | 4 & 5)

# 100 
# 101
# =====
#   100
#   011
# ===========
#     111