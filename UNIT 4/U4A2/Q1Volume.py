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

length = int(input("Please input the length: "))
width = int(input("Please input the width: "))
height = int(input("Please input the height: "))



# PROCESSING

volume = length*width*height

# OUTPUT
print("The volume of your rectangular prism is: " + str(volume))