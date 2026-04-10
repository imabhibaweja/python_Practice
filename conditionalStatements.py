age=12
if(age>18):
    print("You are an adult")
    print("You are allow to drive")
elif(age==18):
    print("you need to give a licence test")
else:
    print("You are minor")
    print("you are not allow to drive")
print("The End of if-else")

#Match case
day = "Sunday"
match day:
    case 'Monday': 
        print("It\'s Monday")
    case 'Tuesday': 
        print("It\'s Tuesday")
    case 'Wednesday': 
        print("It\'s Wednesday")
    case 'Thursday': 
        print("It\'s Thursday")
    case 'Friday': 
        print("It\'s Friday")
    case 'Saturday': 
        print("It\'s Saturday")
    case 'Sunday': 
        print("It\'s Sunday")
    case _:
        print("Nikal Pahli fursat me!!!")