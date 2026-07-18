#ex1:-
def my_function(*names): # *names the args parameter
    for name in names:
        print(name)

my_function("manohar","manu","mano") 

#ex2:-
def my_function(*number):
    for numb in number:
        print(numb)

my_function(7,0,1,3,9,2,3,2,4,3)

def my_function(name,*number):
    print(name)
    for numb in number:
        print(numb)
        

my_function("manohar",7,0,1,3,9,2,3,2,4,3)