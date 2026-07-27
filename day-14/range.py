# using single values argument
x = range(10)
print(x)
print(list(x))
print(tuple(x))

# using two values argument
x = range(3,10) # 3 argument act as starting value and 10 argument act as stopping value
print(x) # here we are printing values in x variable 
print(list(x)) # here we are printing the values in list format 
print(tuple(x)) # here we are printing thhe values in tuple format 

# using three values argument
x = range(3,10,2) # 3 argument act as starting value and 10 argument act as stopping value,2 act as step value
print(x) # here we are printing values in x variable 
print(list(x)) # here we are printing the values in list format 
print(tuple(x)) # here we are printing thhe values in tuple format 

# vrange can be use in for loop is used when we know number of times we need to print 
# ex:-
for i in range(10):
   print(i)

# membership testing in range function 
# ex:-
x = range(10)
print(6 in x)
print(10 in x)