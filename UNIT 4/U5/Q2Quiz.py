# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q2 Quiz
# DATE OF CREATION:  Jan 26, 2022
# PURPOSE OF PROGRAM:  To prompt user to answer a previously created multiple choice question

#Open the file
inFile = open("Q1Questions.txt", 'r')

# VARIABLE DEFINITION

#Reads the lines of the file and assigns them to variables
line1 = inFile.readline()
line2 = inFile.readline()
line3 = inFile.readline()
line4 = inFile.readline()
line5 = inFile.readline()
line6 = inFile.readline()
userInput = 0

# INPUT/PROCESSING/OUTPUT

#Outputs the file's contents
print (line1.strip('\n'))
print ("a) " + (line2.strip('\n')))
print ("b) " + (line3.strip('\n')))
print ("c) " + (line4.strip('\n')))
print ("d) " + (line5.strip('\n')))

#Prompts user for their answer to the question
userInput = input("Please enter either a, b, c or d and I will tell you if it is correct: ")

#Checks if user answered correctly
if userInput == line6:
  print("CORRECT!!!")
elif userInput != line6:
  print("You are incorrect, the correct answer was " + line6)
  
#Closes file
inFile.close()