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
		febSales.append(stringToList[2])
		marSales.append(stringToList[3])
		aprSales.append(stringToList[4])
		maySales.append(stringToList[5])
		junSales.append(stringToList[6])
		julSales.append(stringToList[7])
		augSales.append(stringToList[8])

	#loop over each sales list to create a new list
	januaryInts = listToNums(janSales)
	februaryInts = listToNums(febSales)
	marchInts = listToNums(marSales)
	aprilInts = listToNums(aprSales)
	mayInts = listToNums(maySales)
	juneInts = listToNums(junSales)
	julyInts = listToNums(julSales)
	augustInts = listToNums(augSales)
	
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


	