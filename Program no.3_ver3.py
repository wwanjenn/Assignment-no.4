# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def priceTotal():
    money_ = int(input("How much money do you have?: "))
    priceA = int(input("How much is an apple?: "))
    return money_, priceA

def formulaCalculate(moneyF,appleF,):
    maxAcalculate = moneyF // appleF 
    totalChangecalculate = moneyF % appleF
    return maxAcalculate, totalChangecalculate

# Steps
#1 Input amount of money and price of apple
money, price = priceTotal()
#3 Formula for Total amount of apples and Change
maxApples, totalChange = formulaCalculate(money,price)
#5 Display
display(maxApples,totalChange)