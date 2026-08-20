# single inheritance
class Human:
    def __init__(self,name,age,mouth):
        self.name = name 
        self.age = age 
        self.mouth = mouth 
    def ranjith(self):
        print(f"hello my name is {self.name} and i am {self.age} andi can spean with my {self.mouth} mouth")

class Person(Human):
    pass 

c1 = Person("ranjith",21,1)
c1.ranjith()  