inputvar = input("Type something here:")
stringvar1 = "blep"
intvar = 118
#concatenation
print(inputvar + stringvar1)

#casting
#str() - converts value to string

convertedvar = str(intvar)

#int() - converts to int

textvar2 = input("type in a number:")

convtoint = int(textvar2)

print (convtoint + 5)

#bool() - converts to bool
#float() - converts to float

print(bool('any text')) #this is true
print(bool('')) #empty string is false

print(bool(0)) #Only number to return false

print(3/2)

#% Modulo
print(3%2) #output is 1

#3/2 2 goes into 3 once, 1 remainder
#helps you figure out if a number is whole or not

#other ways to cast data

numvar = 56.5
textvar = "hello, I am"

print(textvar, numvar)
#commas add spaces automatically
