minvar = 1
maxvar = 100
guessedInt = int(input("Enter a number: "))
guessCount=0
while guessedInt < minvar or guessedInt > maxvar:
    print("Try again, that number is either too big or too small")
    guessCount = guessCount + 1
        if guessCount == 3:
            print(None)

