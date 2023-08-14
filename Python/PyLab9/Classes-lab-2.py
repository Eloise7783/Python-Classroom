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
    def transfer(self, amount, object):
        object.deposit(amount)
        self.withdraw(amount)

food = Budget(input("Enter starting Food budget: "))
clothing = Budget(input("Enter starting Clothing budget: "))
entertainment = Budget(input("Enter starting Entertainment budget: "))

optionInput = input("""What would you like to do?
1 - Withdraw
2 - Deposit
3 - View Balance
4 - Transfer funds
Enter a number: """)

if optionInput == "1":
    withdrawInput = input("""Which budget would you like to withdraw from?
    1 - Food
    2 - Clothing
    3 - Entertainment
    """)
    if withdrawInput == "1":
        foodBudgetInput = int(input("Enter the amount to withdraw: "))
        food.withdraw(foodBudgetInput)
        print(foodBudgetInput,"withdrawn")
    elif withdrawInput == "2":
        clothingBudgetInput = int(input("Enter the amount to withdraw: "))
        clothing.withdraw(clothingBudgetInput)
        print(clothingBudgetInput,"withdrawn")
    elif withdrawInput == "3":
        entertainmentBudgetInput = int(input("Enter the amount to withdraw: "))
        entertainment.withdraw(entertainmentBudgetInput)
        print(entertainmentBudgetInput,"withdrawn")
elif optionInput == "2":
    depositInput = input("""Which budget would you like to deposit to?
    1 - Food
    2 - Clothing
    3 - Entertainment
    """)
    if depositInput == "1":
        foodBudgetInput = int(input("Enter the amount to deposit: "))
        food.deposit(foodBudgetInput)
        print(foodBudgetInput,"deposited")
    elif depositInput == "2":
        clothingBudgetInput = int(input("Enter the amount to deposit: "))
        clothing.deposit(clothingBudgetInput)
        print(clothingBudgetInput,"deposited")
    elif depositInput == "3":
        entertainmentBudgetInput = int(input("Enter the amount to deposit: "))
        entertainment.deposit(entertainmentBudgetInput)
        print(entertainmentBudgetInput,"deposited")
elif optionInput == "3":
    balanceInput = input("""Which budget would you like to view the balance of?
    1 - Food
    2 - Clothing
    3 - Entertainment
    """)
    if balanceInput == "1":
        print("The Food budget balance is",food.balance())
    elif balanceInput == "2":
        print("The clothing budget balance is",clothing.balance())
    elif balanceInput == "3":
        print("The entertainment budget balance is",entertainment.balance())
elif optionInput == "4":
    transferFromInput = input(("""Which budget would you like to transfer from?
    1 - Food
    2 - Clothing
    3 - Entertainment
    """))
    if transferFromInput == "1":
        transferAmount = int(input("Enter the amount you'd like to transfer: "))
        transferTo = input("""Which budget would you like to transfer to?
    1 - Clothing
    2 - Entertainment
    """)
        if transferTo == "1":
            food.transfer(transferAmount,clothing)
            print(transferAmount,"transferred to Clothing budget")
        elif transferFromInput == "2":
            food.transfer(transferAmount,entertainment)
            print(transferAmount,"transferred to Entertainment budget")
    elif transferFromInput == "2":
        transferAmount = int(input(("Enter the amount you'd like to transfer: ")))
        transferTo = input("""Which budget would you like to transfer to?
    1 - Food
    2 - Entertainment
    """)
        if transferTo == "1":
            clothing.transfer(transferAmount,food)
            print(transferAmount,"transferred to Food budget")
        elif transferFromInput == "2":
            clothing.transfer(transferAmount,entertainment)
            print(transferAmount,"transferred to Entertainment budget")
    elif transferFromInput == "3":
        transferAmount = int(input(("Enter the amount you'd like to transfer: ")))
        transferTo = input("""Which budget would you like to transfer to?
    1 - Food
    2 - Clothing
    """)
        if transferTo == "1":
            entertainment.transfer(transferAmount,food)
            print(transferAmount,"transferred to Food budget")
        elif transferFromInput == "2":
            entertainment.transfer(transferAmount,clothing)
            print(transferAmount,"transferred to Clothing budget")
