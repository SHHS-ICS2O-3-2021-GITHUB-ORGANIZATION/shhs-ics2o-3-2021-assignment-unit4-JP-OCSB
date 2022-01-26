# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q3 Word Triangle
# DATE OF CREATION:  Jan 25, 2022
# PURPOSE OF PROGRAM:  To print a word triangle with an inputted word

# VARIABLE DEFINITION

userInput = 0
printedLetters = 0
strLength = 0

# INPUT

#prompting user for input of word
userInput = input("Please input a word for me to crate a word triangle out of up to 20 characters long: ")

# PROCESSING/OUTPUT

#Putting the length of the word in a variable.
strLength = len(userInput)

#Printing the word triangle
while strLength > printedLetters:
    printedLetters = printedLetters + 1
    print(userInput[0:printedLetters])