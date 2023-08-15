class Lettercheck:
	def __init__(self,inList):
		self.lettersList = inList
	
	def vowelCheck(self,letter):
		if letter in self.lettersList:
			print("Vowel = ", True)
		else:
			print("Vowel = ", False)

	def consonantCheck(self,letter):
		if letter not in self.lettersList:
			print("Consonant = ", True)
		else:
			print("Consonant = ", False)

stringIn = input("Enter a letter and I'll determine if it's a vowel: ")	
	
vowels = Lettercheck(["a", "e", "i", "o", "u"])

vowels.vowelCheck(stringIn)
vowels.consonantCheck(stringIn)

#vowelList=["a", "e", "i", "o", "u"]

#if letter in vowelList:
	#print(True)

#for indivLetter in self.lettersList:
		#if letter == indivLetter: