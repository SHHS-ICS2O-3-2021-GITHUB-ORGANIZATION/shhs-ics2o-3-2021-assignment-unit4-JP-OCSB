# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM:  Q2 Average
# DATE OF CREATION: January,19,2022
# PURPOSE OF PROGRAM: collects a series of non zero numbers and caluclates the sum and average of them  
import math

# VARIABLE DEFINITION

list = 0
userList = 0

# INPUT

#Asking user for list of numbers
list = input("please enter the series of numbers separated by a space: ")

#Allowing the user to see their average and sum of the numbers by inputting the number 0 
zeroInput = int(input("please enter the number 0 to see your sum and average: "))

# PROCESSING

#Splitting the string of numbers into a list
userList = list.split()

for i in range(len(userList)):
  userList[i] = int(userList[i])

#average = userList // 
listLength = len(userList)
listSum = sum(userList)
listAverage = listSum//listLength

# OUTPUT

#Printing the sum and average
if zeroInput == 0: 
   print("Sum = ", listSum)
   print("average = ", listAverage)

#Checking to see if number is 0
elif zeroInput != 0:
  zeroInput2 = int(input("Please try again: "))
  if zeroInput2 == 0:
    print("Sum = ", listSum)
    print("average = ", listAverage)
  else:
      print("You failed stupid!")
      exit()