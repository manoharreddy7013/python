ex:1.
a = "manohar reddy"
print(len(a))

ex:2.
my_tuple =("p","manohar","reddy")
print(len(my_tuple))

# ex:3.
my_dictionary = {
    "name":"manohar",
    "age": 24,
    "year" : 4
}

# ex:4.
class Phonepay:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
    def paid(self):
        print("paid using phonepay")
class Cash:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
    def paid(self):
        print("paid using cash")
class Card:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
    def paid(self):
        print("paid using card")        

p1 = Phonepay(1,2000)
c1 =Cash(2,3000)
c2 = Card(3,5000)

for i in (p1,c1,c2):
    print(i.account)
    print(i.balance)
    i.paid()