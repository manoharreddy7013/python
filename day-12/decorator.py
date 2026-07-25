def changecase(func):
    def dec():
        return func().upper()
    return dec 

@changecase
def decorator():
    return "manohar"

print(decorator())

# double decorator
def changecase(func):
    def dec():
        return func().upper()
    return dec 

@changecase
def decorator():
    return "manohar"

@changecase
def decorators():
    return "monster"

print(decorator())
print(decorators())

# augment decorator function
def changecase(func):
    def dec(x):
        return func(x).upper()
    return dec 

@changecase
def decoratora(name):
    return "manohar" + name 


print(decoratora(" is an monster"))