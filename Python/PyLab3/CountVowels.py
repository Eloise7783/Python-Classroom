vowelList = ["a","A","e","E","i","I","o","O","u","U"]

inputWord = input("Enter a word:")

wordLength= len(inputWord)
vowelCounter = 0
for letter in range[0, wordLength, 1]:
    if letter in vowelList:
        vowelCounter = vowelCounter+1
print("This word contains",vowelCounter," vowels") 