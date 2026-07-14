day = 4
match day:
    case 1:
        print("this is day one ") 
    case 2:
        print("this is day two ") 
    case 3:
        print("this is day three ") 
    case 4:
        print("this is day four ") 
    case 5:
        print("this is day five ") 
    case 6:
        print("this is day six ")
    case 7:
        print("this is day seven ")  


# match case using |(or) operator
day = 4
match day:
    case 1|2|3|4|5:
        print("week days") 
    case 6|7:
        print("week off ") 

# match case using | (or) operator and if condition statement
month = 1
day = 4
match day:
    case 1|2|3|4|5 if month ==1:
        print("this is month 1 and day 1,2,3,4,5") 
    case 6|7 if month == 2:
        print("this is month 2 and day 6,7 ") 