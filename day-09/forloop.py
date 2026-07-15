fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#for loop using break control statement:-

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break 
  print(x)

#for loop using continue control statement:-
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue  
  print(x)

#for loop using range function:-

for i in range(0,5):
    print(i)

#for loop using else condition statement:-
for i in range(0,5):
    print(i)
else:
    print("finally finished")