#function to turn each list from a list of strings to a list of ints
def listToNums(salesList):
	newList = []
	for l in salesList:
		newList.append(int(l))
	return newList

#lists
companies = []
sales = []
janSales = []
#opens and reads file
with open("Python/PyLab7/carSale.csv","r") as openedFileVar:
	fileAsAString = openedFileVar.readlines() 

	#print(fileAsAString)
	#stringToList = fileAsAString.split(',')

	for x in fileAsAString[1:8]:
		#companies.append(list(map(str,stringToList[0])))
		stringToList = x.split(",")
		companies.append(stringToList[0])
		#monthly sales
		janSales.append(stringToList[1])
		febSales = stringToList[2]
		marSales = stringToList[3]
		aprSales = stringToList[4]
		maySales = stringToList[5]
		junSales = stringToList[6]
		julSales = stringToList[7]
		augSales = stringToList[8]

	januaryInts = listToNums(janSales)
	#loop over each sales list to create a new list

	#janSalesNumber = janSales.remove()
	#janTotal = sum(janSalesNumber)
	print(januaryInts)
	#for l in fileAsAString:
		#print(fileAsAString)
		#manufacturer sales
		#bmwSales = stringToList[0:7]
		#vauxhallSales = stringToList[1:7]
		#mercSales = stringToList[2]
		#vwSales = stringToList[3]
		#fordSales = stringToList[4]
		#print(companies)
		#print(vauxhallSales)


	