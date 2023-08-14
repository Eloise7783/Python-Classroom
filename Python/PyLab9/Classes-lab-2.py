class Budget:
    def __init__(self, startingFunds):
        self.funds = int(startingFunds)
        
    def withdraw(self, amountToTake):
        self.funds = self.funds - amountToTake
        return self.funds
    def deposit(self, amountToAdd):
        self.funds = self.funds + amountToAdd
        return self.funds
    def balance(self):
        return self.funds

food = Budget(50)
clothing = Budget(25)
entertainment = Budget(25)
#food = Budget(input("Enter starting Food budget: "))
#clothing = Budget(input("Enter starting Clothing budget: "))
#entertainment = Budget(input("Enter starting Entertainment budget: "))

#optionInput = print(input("""What would you like to do?
#1 - Withdraw
#2 - Deposit
#3 - View Balance """))

#if optionInput == "1":
#    withdrawInput = print(input("""Which budget would you like to withdraw from?
#    1 - Food
#    2 - Clothing
#    3 - Entertainment"""))
#    if withdrawInput == "1":
#        foodBudgetInput = int(print(input("Enter the amount to withdraw: ")))
#        food.withdraw(foodBudgetInput)

print(clothing.deposit(5))
print(entertainment.withdraw(5))
print(clothing.balance())