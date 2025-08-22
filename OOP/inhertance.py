# # Parent Class
# class Person:
#     def __init__(self , fname , lname):
#         self.fname = fname 
#         self.lname = lname 

#     def printname(self):
#         return self.fname + " " +  self.lname

# class Student(Person):
#     def __init__(self, fname, lname , grade):
#         super().__init__(fname, lname)
#         self.grade = grade
#     def printname(self):
#         return str(super().printname()) + " " + str(self.grade)

# z = Student("Ahmed" , "Hassan" , 4)
# print(z.printname())


# class Shape:
#     def __init__(self , length):
#         self.length = length 
#     def area():
#         pass
#     def getLength(self):
#         return self.length

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(radius)


#     def area(self):
#         return super().getLength()**2 * 3.14
#     def __repr__(self):
#         return "Hello"
#     def __str__(self):
#         return "Gamal"

# C1 = Circle(5)
# print(str(C1))

# class A :
#     def show_a(self):
#         print("Class A")

# class B: 
#     def show_a(self):
#         return("Class B")

# class C(A , B):
#     def show_a(self , b):
#         return b.show_a()
    

# obj = C()
# print(obj.show_a(B()))
