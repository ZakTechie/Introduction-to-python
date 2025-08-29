# list1 = ["apple" , "banana" , "cherry"] # iterable 
# myiter = iter(list1)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# for n in list1:
#     print(n)


class Numbers:
    def __iter__(self):
        self.n = 0 
        return self 
    def __next__(self):
        x = self.n
        self.n += 1
        return x 
    

myNumbers = Numbers()
myiter = iter(myNumbers)

for i in range(1,100):
    print(next(myiter))
    if i == 50:
        raise StopIteration
