#Step 1
#Debug the following program so that it properly takes a users order and outputs the price of the order.

#Step 2
#Edit the existing code and have it print out the items you are ordering as follows...
#Example
# "Coffee x 0"
# "Cake x 2"
# "Tea x 3"

#Step 3
#Have the items you are ordering also output their indavidual cost.
#Example
# "Coffee x 0 : 0.00"
# "Cake x 2 : 5.00"
# "Tea x 3 : 3.6"


listOfOrders = ["Coffee" "Cake" "Tea"]
price = 0
for i in range(len(listOfOrders)):
  message = "Would you like to buy a ", str(listOfOrders[i]), ". Yes / No   "
  myOrder = str( input(message))

  if myOrder == "Yes" and i == 1:
    number = input("How many would you like? ")
    for a in range(number):
      price = price + 2.5

  if myOrder == "Yes" and i == 2:
    number = input("How many would you like? ")
    for a in range(number):
      price = price + 5.2

  if myOrder == "Yes" and i == 3:
    number = int(input("How many would you like? "))
    for a in range(number):
      price = price + 1.2

print("Your total price is", price, ".")