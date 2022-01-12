# NAME OF AUTHOR:  Jacob Pierunek
# NAME OF THE PROGRAM:  Q3Taxs
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
taxandtotalCostOfItems = 0

# INPUT
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

totalValueOfItems = (item1 + item2 + item3 + item4 + item5 + item6 + item7+ item8 + item9 + item10)

taxOnItems = totalValueOfItems*0.13

taxandtotalCostOfItems = taxOnItems + totalValueOfItems

# OUTPUT

print("The value of the items without tax is: $" + str(totalValueOfItems))
print("The value of the tax on the items is: $" + str(taxOnItems))
print("The total value of the tax and the items together is: $" + str(taxandtotalCostOfItems))