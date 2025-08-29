# # global ==> عاوز المتغير اللي بداخل الفانكشن يتشاف برا الفانكشن 
# # nonlocal ==> بستخدمها ف حالة Nested function 

# # مينفعش اعمل اتنين scope لنفس المتغير 
# # a = 100
# # def myfunc():
# #     global a
# #     a = 300 
# #     print(a)

# # myfunc()
# # print(a)

# def func1():
#     global a
#     a = "jane"
#     b = ""
#     def func2():
#         # nonlocal a 
#         nonlocal b
#         a = "Hello"
#         b = a 
#     func2()
#     a = b
#     return b

# print(func1())
# print(a)