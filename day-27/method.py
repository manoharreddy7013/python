class Car:
    def __init__(self,start,front_wheels,back_wheels,gear):
        self.start = start
        self.gear = gear 
        self.front_wheels = front_wheels 
        self.back_wheels = back_wheels
    def Work(self):
        if self.start == True and self.gear == 1|2|3|4:
            print(f"car is started the gear is {self.gear} now its moving front and front_wheels {self.front_wheels} can rotate right or left and back wheels{self.back_wheels} can rotate front")
        elif self.start == True and self.gear == "R":
            print(f"car is started the gear is {self.gear} now its moving back and front_wheels {self.front_wheels} can rotate right or left and back wheels{self.back_wheels} can rotate back")
        else:
            print("car is not started")

c1 = Car(True,2,2,"R")
c1.Work()