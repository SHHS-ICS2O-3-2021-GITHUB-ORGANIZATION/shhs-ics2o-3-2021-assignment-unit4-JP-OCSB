# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q2 Math Drill
# DATE OF CREATION:  Jan 21, 2022
# PURPOSE OF PROGRAM:  To help user practice math skills
import random
# VARIABLE DEFINITION

decider = 0
num1 = 0
num2 = 0
reDo = 1

# PROCESSING

#Using while statement for continuation of the program
while reDo == 1:
#Choosing whether it is an addition or multiplication question
  decider = random.randint(1,2)
    
  if decider == 1:
    print("You will be getting a multiplication questions!")
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    print(num1, num2)
    answer = int(input("Please multiply the two numbers above and enter your answer for the question here: "))
     #checking if answer is correct
  if answer == (num1*num2):
        print("YAY! you got it correct")
        reDo = int(input("Input 1 to continue with another question enter 0 to exit: "))
        #checking if answer is wrong.
  if answer != (num1*num2):
            print("OOPS! you got it wrong")
            reDo = int(input("Input 1 to continue with another question enter 0 to exit: "))
    
    
  elif decider == 2:
    print("You will be getting an addition questions!")
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(num1, num2)
    answer = int(input("Please add the two numbers above and enter your answer for the question here: "))
    #checking if answer is correct.
    if answer == (num1+num2):
        print("YAY! you got it correct")
        reDo = int(input("Input 1 to continue with another question enter 0 to exit: "))
  #checking if answer is wrong.
        if answer != (num1+num2):
            print("OOPS! you got it wrong")
            
            reDo = int(input("Input 1 to continue with another question enter 0 to exit.: "))
    

# INPUT





# PROCESSING





# OUTPUT