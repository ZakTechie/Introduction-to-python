import re 

# match(pattern , string) ==> بيشوف هل النص بدايته بالنمط اللي انا بدور عليه ولا لا

# txt = "dog and cat"
# result = re.match(r"dog" , txt)

# print(result)


# search() ==> بيشوف اول تطابق اي كان مكانه

# txt = "dog and  concatenation cat" 

# result = re.search(r"cat" , txt)
# print(result)

# findall()
# txt = "dog and  concatenation cat" 

# result = re.findall(r"cat" , txt)
# print(result)


# sub() ==> used for replace 

# txt= "I like cats and cats"
# new_text = re.sub(r"cats" , "dogs" , txt)

# print(new_text)

# \w+@\w+.(com|org)
# [a-z]+@[a-z]+.(com|org)
# t = "Contact us at info@example.com or support@test.org or Zack@yahoo.net"
# emails = re.findall(r"(\w+@\w+.(com|org))" , t)
# print(emails[0][0])

# ([+]966)\s(\d+)

# txt = """
#     Name : Ali, Age: 30; Name: Gamal, Age:25
# """

# # result = re.search(r"([+]966)\s(\d+)" , txt)
# result = re.findall(r"Name\s?: (\w+), Age:\s?(\d+)" , txt)

# print(result)



# text = "Product: Laptop, Price: 1200$\nProduct: Mobile, Price: 1300$"
# result = re.findall(r"Product: (?P<item>\w+), Price: (?P<price>\d+)" , text)

# print(result[0].group("item"))
# print(result[1].group("price"))

# Task :
# for n in result:
#     for i in range(len(n)):
#         print(f"Product: {n[i]} \t Price: {n[i]}$")


# text = "2025-09-05"
# result = re.findall(r"""
#         (\d{4}) # السنة
#                 -  # دا للشرطة اللي بتفصل ما بين السنة والشهر 
#                 (\d{2})
#                 -
#                 (\d{2})
#     """ , text , re.VERBOSE)
# print(result) 

# text = "مرحبا 123 hello"
text = "Hello"
print(re.findall(r"[a-z]" , text ,  re.ASCII))

