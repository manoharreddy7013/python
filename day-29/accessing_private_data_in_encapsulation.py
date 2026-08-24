# accessing the privatize data by creating another method
class Dat:
    def __init__ (self,name,age):
        self.name = name 
        self.__age = age # private data 

    def get_age(self):
        return self.__age
    
d2 = Dat("manohar",24)
print(d2.name)
print(d2.get_age())