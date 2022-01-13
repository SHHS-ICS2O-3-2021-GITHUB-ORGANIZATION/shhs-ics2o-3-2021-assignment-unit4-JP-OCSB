# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q3Taxes
# DATE OF CREATION:  Jan 12, 2022
# PURPOSE OF PROGRAM:  To calculate and display the tax on ten items combined


# VARIABLE DEFINITION

item1 = 0
item2 = 0
item3 = 0
item4 = 0
item5 = 0
item6 = 0
item7 = 0
item8 = 0
item9 = 0
item10 = 0
totalValueOfItems = 0
taxOnItems = 0
taxAndTotalCostOfItems = 0

# INPUT

#Prompting user for the input of the items and assigning them to variables
item1 = float(input("Please input the cost of the first item: "))
item2 = float(input("Please input the cost of the second item: "))
item3 = float(input("Please input the cost of the third item:  "))
item4 = float(input("Please input the cost of the fourth item:  "))
item5 = float(input("Please input the cost of the fifth item:  "))
item6 = float(input("Please input the cost of the sixth item:  "))
item7 = float(input("Please input the cost of the seventh item:  "))
item8 = float(input("Please input the cost of the eigth item:  "))
item9 = float(input("Please input the cost of the ninth item:  "))
item10 = float(input("Please input the cost of the tenth item:  "))

# PROCESSING

#Calculating all value of items involved
totalValueOfItems = (item1 + item2 + item3 + item4 + item5 + item6 + item7+ item8 + item9 + item10)

taxOnItems = totalValueOfItems*0.13

taxAndTotalCostOfItems = taxOnItems + totalValueOfItems

#Rounding values to two decimal places
totalValueOfItems = round(totalValueOfItems, 2)

taxOnItems = round(taxOnItems, 2)

taxAndTotalCostOfItems = round(taxAndTotalCostOfItems, 2)

# OUTPUT

#Displaying values to user
print("The value of the items without tax is: $" + str(totalValueOfItems))
print("The value of the tax on the items is: $" + str(taxOnItems))
print("The total value of the tax and the items together is: $" + str(taxAndTotalCostOfItems))