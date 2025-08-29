import datetime

# date = datetime.datetime.now()
date = datetime.datetime(2018 , 5 , 14 , 4 , 50 , 10 , 100)
# print(date)
# print(date.month)
# print(date.hour)
print(date.strftime("%a - %d"))

# %a  ==> fri
# %A ==> Friday
# %w ==>  0-6
# %d ==> number of day in month
# %b ==> Aug
# %B ==> August
# %m ==> number of month
# %y ==> 25
# %Y ==> 2025
# %H ==> 0-23
# %I ==> 0-12
# %p
# %M
# %S
# %f 
# %z
# %Z
# %j 
# %U  ==> sunday first day in week 
# %W ==> monday first day in week 
# %c 
# %C
# %x
# %X
# %G 
# %u
# %V