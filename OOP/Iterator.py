# # # __iter__()
# # # __next__()

# mytuple = ("apple" , "banana" , "cherry")
# myiter = iter(mytuple)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # # print(next(myiter))

# # mystring = "Ahmed"
# # myiter = iter(mystring)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))


# # for n in mytuple:
# #     print(n)

# for n in range(len(mytuple)):
#     print(next(myiter))


class Numbers:
    def __iter__(self):
        self.a = 1 
        return self
    def __next__(self):
        if self.a <= 10 :
            x = self.a 
            self.a += 1 
            return x
        else:
            raise StopIteration

n = Numbers()
myiter = iter(n)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))