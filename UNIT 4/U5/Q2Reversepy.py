# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q2 Reverse
# DATE OF CREATION:  Jan 25, 2022
# PURPOSE OF PROGRAM:  To print out an inputed word backwards

# VARIABLE DEFINITION.

UserInput = 0
wordLength = 0

# INPUT

#Prompting user to enter word
userInput = input("Please input a word for me to spell backwards: ")

#Putting the length of the word in a variable
wordLength = len(userInput)

# PROCESSING/OUTPUT

while wordLength > 0:
    #Changing the wordLength variable each time
    wordLength = wordLength - 1
    
    #Printing the word one letter at a time backwards
    print(userInput[wordLength])