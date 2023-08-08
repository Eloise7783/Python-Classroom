# final balance = initial balance(1+interest rate/compounding frequency)compounding frequency*number of years
# initial balance = £100
# interest rate = 10%
# compounding frequency = how often is interest added (annually etc)
# number of years = what we want to calculate
# number of years = Natural Log(Future Value / Present Value) / Natural Log (1 + Interest Rate)

#from math import log
finalBalance = 1000
initialBalance = 100
interestRate = finalBalance/initialBalance
#interestRate = finalBalance/initialBalance

#numOfYears = log(finalBalance / initialBalance) / log(1 + interestRate)

#print("The number of years is", numOfYears)

#numOfYears = log(finalBalance / initialBalance) / log(1 + interestRate)

#print("The number of years is", numOfYears)
finalBalance = int(input("Input the final balance you are aiming for: "))
initialBalance = int(input("Input your initial investment: "))
interestRate=float(input("Input the interest rate in decimal: "))

numOfYears = 0
while initialBalance < finalBalance:
    numOfYears = numOfYears +1
    initialBalance = initialBalance*interestRate
print("The number of years is", numOfYears)



