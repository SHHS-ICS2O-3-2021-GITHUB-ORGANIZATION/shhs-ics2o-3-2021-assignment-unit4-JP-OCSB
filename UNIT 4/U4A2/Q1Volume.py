# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Volume of a Rectangular Prism
# DATE OF CREATION:  Jan 12, 2022
# PURPOSE OF PROGRAM:  To find the volume of a rectangular prism


# VARIABLE DEFINITION

length = 0
width = 0
height = 0
volume = 0

# INPUT

#Prompt user for the length, width, and height and assigning them to variables
length = int(input("Please input the length: "))
width = int(input("Please input the width: "))
height = int(input("Please input the height: "))

# PROCESSING

#Calculating volume
volume = length*width*height

# OUTPUT

#Display volume to User
print("The volume of your rectangular prism is: " + str(volume))