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