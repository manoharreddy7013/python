# ex:-
class Human:
    def __init__(self,eyes,legs,nose,mouth):
        self.eyes = eyes 
        self.legs = legs 
        self.nose = nose 
        self.mouth = mouth 
    def Man(self):
        print(f"all human consists of {self.eyes} {self.legs} {self.nose} {self.mouth}")

c1 = Human(2,2,1,1)
c1.Man()

# there is no rule to be use self only we can use any parameter in place of self but it should be in first place 
# ex:-
class Car:
    def __init__(carparts,wheels,lights,breaks,mirrors):
        carparts.wheels = wheels 
        carparts.lights = lights 
        carparts.breaks = breaks
        carparts.mirrors = mirrors

    def Total(all):
        print(f"car consists of all parts like {all.wheels} {all.lights} {all.breaks} {all.mirrors}")

c2 = Car(4,2,1,2)
c2.Total()