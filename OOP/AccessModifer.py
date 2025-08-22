# # # # # class Person :
# # # # #     def __init__(self , name):
# # # # #         self._name = name # protected

# # # # # p = Person("Ahmed")
# # # # # print(p._name)

# # # # class Person :
# # # #     def __init__(self , name):
# # # #         self.__name = name # private


# # # # p = Person("Ahmed")
# # # # print(p._Person__name)


# # class A:
# #     def hello(self):
# #         print("Hello from " , self.__class__.__name__)

# # class B (A):
# #     pass
# # class C(A):
# #     pass

# # class D(C , B):
# #     pass

# # # d = D()
# # # d.hello()
# # # print(D.mro())

# # a = B()
# # a.hello()



# # # class Person:
# # #     def __str__(self):
# # #         return "Hello in my class"

# # #     def __repr__(self):
# # #         return "Hello in my Class"
    
# # # P= Person()
# # # print(repr(P))

# print(help(filter))