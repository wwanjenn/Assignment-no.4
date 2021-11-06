# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def getAmountAppleOrange():
    apples_ = int(input("How many apple do you want to buy?: "))
    oranges_ = int(input("How many oranges do you want to buy?: "))
    return apples_, oranges_

def calculateFormula(apples_,oranges_):
    apples_ * 20 + oranges_ * 25
    return
    
# Steps
# Ask how many apples and oranges you want to buy?
apples, oranges = getAmountAppleOrange()
#Calculate

# Display
