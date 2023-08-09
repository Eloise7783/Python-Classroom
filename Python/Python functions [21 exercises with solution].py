# 1. Write a Python function to find the maximum of three numbers.
def maxOfThree():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))
    maximum = max(num1,num2,num3)
    print("the maximum of these three numbers is", maximum)

print(maxOfThree())
# 2. Write a Python function to sum all the numbers in a list.
def sumOfNumbers():
    #gather a string of numbers from user
    stringList = input("Please enter the list of numbers you wish to sum, separated by commas: ")
    #turn that string into a list using .split
    numList = stringList.split(",")
    #sum the list using maths function
    print()
    #finalSum = sum(numList)
    #return the output
    print(finalSum)

print(sumOfNumbers())