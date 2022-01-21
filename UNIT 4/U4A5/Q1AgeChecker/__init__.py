# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q1 Age Checker
# DATE OF CREATION:  Jan 21 2022
# PURPOSE OF PROGRAM:  To tell user what section of school or workplace they are in

# VARIABLE DEFINITION

userAge = 0

# INPUT

#Prompt user for their age
userAge = int(input("Please enter your age: "))

# PROCESSING/OUTPUT

#See if user is in elementary school
if userAge == 5 or userAge < 11:
    print("You are in Elementary school")

#See if user is in secondary school
elif userAge == 12 or userAge < 14:
    print("You are in secondary school")

#See if user is in highschool school
elif userAge == 15 or userAge < 18:
    print("You are in highschool")

#See if user is in university/college/workplace
elif userAge > 19:
    print("You are in university/college/workplace")
    
