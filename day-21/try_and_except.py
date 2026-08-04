# example for try and except:-
try:
    print(x)# here try block raises but except block executed
except:
    print("the is no data for x so except block is executed")


# ex2:-
try:
    print(x)# here try block raises but except block executed
except NameError:
    print("except nameerror is executed")
except:
    print("the is no data for x so except block is executed")