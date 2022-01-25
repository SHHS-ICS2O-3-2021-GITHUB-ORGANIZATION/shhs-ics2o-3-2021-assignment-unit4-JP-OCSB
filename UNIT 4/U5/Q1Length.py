# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q1Length
# DATE OF CREATION:  Jan 24, 2022
# PURPOSE OF PROGRAM:  To give the length of a word inputted by the user

# VARIABLE DEFINITION.

userInput = 0
lenOfWord = 0

# INPUT/PROCESSING/OUTPUT.

while True:

  #Asking user for input of word or if they would like to quit
  userInput = input("Please enter a word or type quit to exit: ")

  #Exiting the program if the user inputs "quit"
  if userInput == "quit":
    print("Thank you for using this tool, goodbye")
    exit()

  #Calculating length of word inputed
  lenOfWord = len(userInput)

  #Changing length of word to string
  lenOfWord = str(lenOfWord)

  #Printing length of word
  print("Your word is " + lenOfWord + " characters long")