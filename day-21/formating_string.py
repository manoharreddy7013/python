# formatting string:-
# ex:-
a = "manohar"
print(f"{a} is a student, he completed his b.tech in 2026")

# ex2:-
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# ex3:-
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
