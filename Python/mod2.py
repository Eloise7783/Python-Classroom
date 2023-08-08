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

#len

invar1 = input("type a word: ")
lettercount = len(invar1)
reverseword = '' #empty variable to be assigned later
for indexitem in range(lettercount -1, -1, -1): #-1 is needed because invar1 is base 0 and lettercount is base 1
    reverseword = reverseword + invar1[indexitem]
print(invar1[indexitem])

#list functions
listvar1 = [2,3,4,5,6,7,8,9]
#list.append(object)
listvar1.append(7)
#list.remove(value)
listvar1.remove(3)
#list.insert(index,object)
listvar1.insert(1,2)
#list.count(value)
print(listvar1.count(2))

print(listvar1)
#making a string into a list
listitems = "Dozey.Beakey.Mick.Titch"
print(listitems.split('.'))
#creating a string from a list
separator = ';'
print(separator.join(listitems))

#'in' test

drinks = ["coffee", "tea", "water"]
drinktest = input("What would you like to drink? ")
if drinktest in drinks:
    print ()