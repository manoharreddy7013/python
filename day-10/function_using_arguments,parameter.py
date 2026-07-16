# function using argument
def verify(valid):
    return(valid + "reference")

print(verify("mail")) # here mail is the argument that are passed to function


# function using parameter
def full_name(first_name,last_name):# first_name,last_name are the parameters 
    return first_name + last_name 

print(full_name("manohar","reddy")) # manohar,reddy are the arguments 


# function using default argument
def full_name(first_name,last_name = "reddy"):# first_name,last_name are the parameters and reddy is default argument 
    return first_name + last_name 

print(full_name("manohar"))# manohar are the argument

