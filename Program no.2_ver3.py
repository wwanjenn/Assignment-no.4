# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def getAmountAppleOrange():
    applesA = int(input('How many apple do you want to buy?: '))
    orangesA = int(input('How many oranges do you want to buy?: '))
    return applesA, orangesA

def calculateFormula(applesB,orangesB):
    return applesB * 20 + orangesB * 25
    
    
def display(apples_, oranges_,totalPrice_):
    print(f'The total amount for {apples_} apples and {oranges_} oranges is {totalPrice_}.')

# Steps
# Ask how many apples and oranges you want to buy?
apples, oranges = getAmountAppleOrange()
#Calculate
totalPrice = calculateFormula(apples,oranges)
# Display
display(apples, oranges, totalPrice)