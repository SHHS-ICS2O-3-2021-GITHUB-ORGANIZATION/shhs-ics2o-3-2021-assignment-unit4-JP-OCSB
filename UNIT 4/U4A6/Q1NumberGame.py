# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Number game
# DATE OF CREATION:  Jan 24, 2022
# PURPOSE OF PROGRAM:  To play a number guessing game with the user

import random

# VARIABLE DEFINITION

maxNum = 0
minNum = 0
rightAnswer = 0
tries = 0
goAgain = 0
userGuess = 0

# INPUT

#Prompting user to input the max and min of the number range
maxNum = int(input("Please input the maximum you would like the random number to be: "))
minNum = int(input("Please input the minimum you would like the random number to be: "))

# PROCESSING/OUTPUT

#Creating random number within range given by user
rightAnswer = random.randint(minNum,maxNum)

#Creating loop for user to guess in until they get it right
while goAgain == 0:
    userGuess = int(input("GUESS A NUMBER BETWEEN THE RANGE YOU SPECIFIED:"))
    
    #Checking to see if user is correct
    if userGuess == rightAnswer:
        print("CORRECT!\nYOU WIN")
        #Telling program not to run again because user guessed the number correctly
        goAgain = 1
        
        #Adding try to the try counter to be displayed at the end
        tries = tries + 1
        
        #Telling user how many tries it took them
        print("GAME OVER YOU WON!!! \nTRIES TAKEN: " + str(tries))
        exit()
        
        #Prompting user to try again if they are incorrect
    elif userGuess != rightAnswer:
        print("NOT CORRECT")
        
        #Adding try to the try counter to be displayed at the end
        tries = tries + 1
        
        print("TRY AGAIN")