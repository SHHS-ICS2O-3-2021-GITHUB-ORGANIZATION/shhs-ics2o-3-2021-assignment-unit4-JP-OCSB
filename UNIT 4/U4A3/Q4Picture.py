# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q4Picture
# DATE OF CREATION:  Jan 14, 2022
# PURPOSE OF PROGRAM:  To create a simple two dimensional pictue
#import pygame module
import pygame
from pygame import Color
from pygame import Rect
from pygame import draw

#initialization
pygame.init()

# VARIABLE DEFINITION

gameDisplay = 0

# PROCESSING

#creates canvas
gameDisplay = pygame.display.set_mode((500, 500))

gameDisplay.fill(Color('lightblue'))

# OUTPUT

#draw red rectangle
draw.rect(gameDisplay, Color('red'), Rect(100, 200, 300, 200))

#draw yello roof (triangle)
draw.polygon(gameDisplay, Color('yellow'), [(100, 200), (400, 200), (250, 50)])

#draw blue door (rectangle)
draw.rect(gameDisplay, Color('blue'), Rect(300, 250, 40, 70))

#updates entire canvas
pygame.display.update()