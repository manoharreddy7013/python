#ex:-
def my_scope():
    x = 10 # variable is created inside function so it is available only inside function 
    print(x)

my_scope()
#ex2:-
def my_scope():
    x = 10 # variable is created inside function so it is available only inside function 
    def inner_scope():
        print(x)

    inner_scope()

my_scope()

#ex:-
x = 15 #this is a variable that written in main body of python code and its a global scope it can be accessed both inside and outside of afunction 
def my_function():
    print(x)

my_function()
print(x)

#named scope
x = 15
def my_function():
    x = 20
    print(x)

my_function()
print(x)