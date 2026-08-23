# method overriding
class Animal:
    def sound(self):
        print("animal sounds")

class Cat(Animal):
    def sound(self):
        print("cat sounds meow")

c1 = Cat()
c1.sound()

# we can extract the parent properties using super().parent function name 
# it helps in bringing parent properties along with the child properties
class Animal:
    def sound(self):
        print("animal sounds")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("dog sounds barks")

d1 = Cat()
d1.sound()

