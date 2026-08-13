# simple class
class my_class:
    x = 10

print(my_class)

# class with object
class human:
    a = 1
    b = 2
    c = 3
    d = 4

h1 = human()
print(h1.a) 
print(h1.b) 
print(h1.c) 
print(h1.d) 

# creating class,method,object 
# ex:-
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello my name is {self.name}"

p1 = Person("manohar",24)
print(p1.greet()) 
     