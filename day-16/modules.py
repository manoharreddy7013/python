import my_modules  
my_modules.data("manohar")

a = my_modules.names["name"]
print(a)

# using from built inn function to import specific data inside a module
from my_modules import names 
print(names["age"])