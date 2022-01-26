# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q1 Questions
# DATE OF CREATION:  Jan 25, 2022
# PURPOSE OF PROGRAM:  To create a multiple choice question and save it in a file

#Opening a text file
filehandle = open("Q1Questions.txt",'w')

# VARIABLE DEFINITION

question = 0
answera = 0
answerb = 0
answerc = 0
answerd = 0
rightAnswer = 0

# INPUT

# Prompting user to enter the question
question = input ("Enter your question: ")

# PROCESSING/INPUT

#Writing question in the text file
filehandle.write(question + "\n")
 
#Prompting user to enter one possible answers to the question
answera = input("Enter the first possible answer you will have four possible answers in total (a): ")

#Writing the possible answer in the text file
filehandle.write(answera + "\n")

#Prompting user to enter one possible answers to the question
answerb = input("Enter the second possible answer (b): ")

#Writing the possible answer in the text file
filehandle.write(answerb + "\n")

#Prompting user to enter one possible answers to the question
answerc = input("Enter the third possible answer (c): ")

#Writing the possible answer in the text file
filehandle.write(answerc + "\n")

#Prompting user to enter one possible answers to the question
answerd = input("Enter the fourth and final possible answer (d): ")

#Writing the possible answer in the text file
filehandle.write(answerd + "\n")

#Prompting user to enter the correct answer
rightAnswer = input("Enter the correct answer in letter form, ex.a: ")

#Writing the correct answer in the text file
filehandle.write(rightAnswer)
 
#Closing the file
filehandle.close()

# OUTPUT

#Printing finishing statement
print("Yay!!, You have successfully created a multiple choice question")