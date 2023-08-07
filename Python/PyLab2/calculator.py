num1 = float(input("input first number"))
num2 = float(input("input second number"))
print("-----")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s ")
print("-----")
operation = input("Choose an operation: ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "s":
    print(num1 ** num2)
