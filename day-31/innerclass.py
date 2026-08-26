class Outer:
    def __init__(self):
        self.name = "manohar" 

    class Inner:
        def __init__(self):
            self.name1 = "nenu" 

        def display(self):
            return self.name1

c1 = Outer()
c2 = c1.Inner()
print(c2.display())
print(c1.name)

# practical example code
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand 
        self. model = model
        self.Car = self.Car()
    class Car:
        def __init__(self):
            self.status = "off"

        def start(self):
            self.status = "on"
            print("engine on")

        def stop(self):
            self.status = "off"
            print("engine off")

        def drive(self):
            if self.status == "on":
                print(f"{self.brand} car model{self.model} is driving now")
            else:
                print("engine not started")

v = Vehicle("tata","sierra")
v.Car.drive()
v.Car.start()