x = lambda a,b: a*b 
print(x(10,5))
#using lambda function
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))