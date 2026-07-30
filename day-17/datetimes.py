import datetime

x = datetime.datetime.now()
print(x)

# printing year and day 
# ex:-
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# # creating date module 
# # ex:-
x = datetime.datetime(2026,7,31)
print(x)

# # creating date module 
# # ex:-
x = datetime.datetime(2026,7,31)
print(x.strftime("%B"))