"""
import random
rightAnswer = random.randint(1, 10)
counter = 5
while counter > 0:
    print("GUESS A NUMBER BETWEEN 1-10:")
    number = input()
    number = int(number)
    if number == rightAnswer:
        print("CORRECT!\nYOU WIN")
        exit()
    elif number != rightAnswer:
        print("NOT CORRECT")
        counter = counter - 1
        print("lives remaining:",counter)
print("GAME OVER\nright answer was " + str(rightAnswer))
"""