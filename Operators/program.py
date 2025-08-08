# # Arithmetic operator  Done
# # Assignment operator  Done
# # Comparison Operator  Done
# # Logical Operator  Done
# # Identitiy operator Done
# # Membership operator  Done
# # Bitwise Operator 


# # num1:int = 4 
# # num2 = 5 

# # # + - * / % ** // floor division

# # print(num1 + num2) # 9 
# # print(num1 - num2) # -1
# # print(num1 * num2) # 20
# # print(num1 / num2) # 0.8 
# # print(num1 % num2) # 4 
# # print(num1 ** 2) # 16
# # print(num1 // num2) # 0

# # print(5 // 4) 


# # Assignment operator
# # = 
# # +=
# # -=
# # *=
# # /=
# # %=
# # **=
# # //=
# # &=
# # |=
# # ^=
# # >>=
# # <<=
# # :=

# # n = 3 
# # # n = n + 3  n += 3 
# # # n = 3 - n 
# # #  n -= 3

# # # n = 3 * n 
# # # n *= 3 

# # # n //= 4 # 0 

# # # n %= 2 # 1
# # n ^= 4 
# # print(n)
# # T & T ==> T
# # F & T ==> F
# #  16 8 4 2 1
# #  0 0 0 1 1   ==  3
# #  0 0 1 0 0 == > 4 
# # ==============
# # 00000  ==> 0

# # # >>= Right shift operator 
# # n = 5
# # n >>= 2

# # print(n)
# # #  5 / 4

# # # <<= Left shift operator
# # n = 5 
# # n <<= 2 
# # #  5 * 4
# # print(n) # 20 

# # print(x:=3)

# # z = 3 
# # # print(z)

# # print(z:=3)

# # Comparison operator 
# # ==  Equal
# # !=  Not Equal
# # > 
# # <
# # >=
# # <=

# # n = 3 
# # z = 4 
# # print(n != z)

# # Logical operator 
# # and 
# # not 
# # or
# # num= bool(input("Enter any number: "))
# # if(not num):
# #     print("between 4 and 10")
# # else:
# #     print("None")

# # num = 0 
# # con = bool(num)
# # print(con)

# # identity operator 
# # is 
# # is not 
# # x = "Ahmed"
# # y = "Ali"
# # print(x is  y)


# # Membership operators 
# # in 
# # not in 

# # z = ["apple" , "banana"]
# # print("banana" in z)

# # users = ["Ahmed" , "Ali" , "Dina"]
# # name = input("Enter your username: ")
# # if(name in users):
# #     print("login Successfully")
# # else:
# #     print("Not allowed to login")

# # bitwise operator
# # &
# # | 
# # ^
# # ~
# # <<
# # >>

# # print(~3)
# # # 011 ==> 100 == -4

# # print(100 + ~3) # 100 - 4 

# # operator priority = precdence
# # print((6+3) - (6+3)) # 0 
# # print(100 + 5 * 3) # 115

# # 1- ()
# # 2- **
# # 3- +z -z ~z
# # 4- * / // %
# # 5- + -
# # 6- << >>
# # 7- &
# # 8- ^
# # 9- |
# # 10- indenitity and comparison , membership 
# # 11- not 
# # 12- and 
# # 13- or 

# n = 4
# # print((4**2) + 7 -n // 2 & n) # 16 + 7 + 4 
# # 16 + 7 - 2 & 4
# # 110
# # 100 
# # 100


# print((4**2) + 7 - n // 2 & n)
# # 16 + 7 - 2 & 4  
# # 23 - 2 = 21
# # 21 & 4  ==

# #  16 8 4 2 1
# #  1  0 1 0 1
# #  0  0 1 0 0 
# #  0  0 1 0 0 