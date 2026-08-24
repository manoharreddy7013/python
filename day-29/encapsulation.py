# encapsulation
class Data:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age # private data 
    
d1 = Data("manohar",24)
print(d1.name)
print(d1.__age) # occurs an error because age data is privatized

