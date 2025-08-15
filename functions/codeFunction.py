# # def my_function(**param):
# #     print(param["fname"])

# # # my_function("Ahmed" , "Ali" , "Ibrahim" , "Mohamed")
# # my_function(fname= "Ahmed" , lname="Ali")

# # def func( name , coutnry= "Egypt" ):
# #     print()


# Thenames = ["Gamal" , "Ali" , "Ibrahim"]
# def my_fun(names):
#     for n in names:
#         print(n)

# my_fun(Thenames)

# def my_function(z , v , b , /):
#     print(z , v , b)

# my_function(z = 4 , v = 5 , b= 6 )


# def my_functions(* , z , v , b):
#     print(z , v , b)

# my_functions(z=4,v=5,b=6)

# / *
# def my_function(a , b , c , d):
#     print(a + b+c +d) 

# my_function(9,12,c =8 ,d=9)


# Recursion 

# 1+2+3+4

def sum(k):
    if k > 0 :
        re = k + sum(k-1)
    else:
        return k 
    return re 

print("Recursion : " , sum(5))

# sum(5)
# 5 + sum(4)
#  5 + 4 + sum(3)
# 5 + 4 + 3 + sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 1 + sum(0)
# 5 + 4 + 3 + 2 + 1 +  0