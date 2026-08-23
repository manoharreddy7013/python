# multiple inheritance
class Father:
    def father(self):
        print("hello i teaches maths")
        
class Mother:
    def mother(self):
        print("mother teaches physics")
        

class Child(Father,Mother):
    def child(self):
        print("child teaches chemistry")

c1 = Child()
c1.father()
c1.mother() 
c1.child()

# multi level inheritance
class Grand_father:
    def grandfather(self):
        print("grand father consists of 10 acres land")
class Father(Grand_father):
    def father(self):
        print("grand father consists of 20 acres of land")
class Sons(Father):
    def son(self):
        print("now i earned 25 acres now total i have")

s1 = Sons()
s1.grandfather()
s1.father()
s1.son()

