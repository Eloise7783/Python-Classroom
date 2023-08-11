minvar = 1
maxvar = 100
guessCount=0
while guessCount<=2:
    guessedInt = int(input("Enter a number: "))
    if guessedInt < minvar or guessedInt > maxvar:
        print("Try again, that number is either too big or too small")
        guessCount = guessCount + 1
    else:
        print(guessedInt)
        break
if guessCount == 3:
            print(None)

