# using __init__()
#ex:-
class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 


d1 = Dog("tommy",10)
print(d1.name)
print(d1.age)

class Pog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def Animal(self):
        return f"hello i am {self.name} and i am {self.age} years old"

d3 = Pog("tommy",10)
print(d3.Animal())

# without using __init__()
# ex:-
class Hog:
    pass 

d2 = Hog()
d2.name = "manchi"
d2.local = "true"
print(d2.name)
print(d2.local) 
