# 1st method
x = open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r")
print(x.read())
x.close()

# 2nd method
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r") as f:
    print(f.read())

# 3rd method to print specific number of characters
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r") as f:
    print(f.read(5))

# 4th method to print specific number of line
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r") as f:
    print(f.readline())

# using loop in file handling
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r") as f:
    for j in f:
        print(j.read())

# appending the data  
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","a") as f:
    f.write("this is new data added to end of the existed file data")

# open the file after adding  data to exist data file
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","r") as f:
    print(f.read())


# "w" :- overwriting the data to an existing file data
with open("C:/Users/manoh/OneDrive/Desktop/python series/day-32/myfiles.txt","w") as f:
    f.write("this is new data which is overwriiten the old existed data")

# "x" :- used to create the new file if file exists already then it throws error
m = open("newfile.txt","x")

# deleting the python file 
# by importing os and using remove function
imoprt  os 
os.remove("file name")

# deleting entire folder 
# to delete entire folder  we use rmdir() function
import os 
os.rmdir("folder name")
