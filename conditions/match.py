# match exp : 
    # case x : 
        # code 

day = int(input("Enter number"))
month = 7
# Guards
match day:
    case 1 | 2 | 3 |4 if month == 4:
        print("Monday")
    case 5:
        print("Tuesday")
    case _:
        print("Default value")

