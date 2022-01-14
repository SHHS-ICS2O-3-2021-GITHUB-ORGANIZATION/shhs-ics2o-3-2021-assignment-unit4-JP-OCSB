# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q2RandomRange
# DATE OF CREATION:  Jan 14, 2022
# PURPOSE OF PROGRAM:  To take 2 inputed numbers and create a random number between them
import random

# VARIABLE DEFINITION
number1 = 0
number2 = 0
ranNumber= 0

# INPUT

#Prompt user for the two numbers
number1 = int(input("Please input the first number: "))
number2 = int(input("Please input the second number: "))

# PROCESSING

#Creating random number
ranNumber = random.randint(number1,number2)




# OUTPUT
print("The random number within your range is: " + str(ranNumber))