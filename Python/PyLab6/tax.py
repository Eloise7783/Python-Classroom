def getIncomeTax(salary):
    if salary < 11850:
        incomeTax = 0
    elif salary > 11850 and salary < 34500:
        incomeTax = 20% salary * salary / 100
    elif salary > 34501 and salary <= 150000:
        incomeTax = 40% salary * salary / 100
    elif salary > 150000:
        incomeTax = 45% salary * salary / 100
    print("Your annual income tax will be",incomeTax)

wages = int(input("Please enter your annual wage without commas: "))
print(getIncomeTax(wages))