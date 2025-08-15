# class MyClass:
#     z = 5

# p = MyClass()
# print(p.z)


class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age
    def __str__(self):
        return f"{self.name} \t : {self.age}"
    def print(self):
        print("Hello my name is " + self.name)

p1 = Person("Gamal" , 43)
# print(p1.name)
# print(p1.age)

p1.print()