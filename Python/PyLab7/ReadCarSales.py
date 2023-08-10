#function to turn each list from a list of strings to a list of ints
def listToNums(salesList):
	newList = []
	for l in salesList:
		newList.append(int(l))
	return newList

#declaring the lists
companies = []
sales = []
janSales = []
febSales = []
marSales = []
aprSales = []
maySales = []
junSales = []
julSales = []
augSales = []

bmwSales = []
vauxhallSales = []
mercSales = []
vwSales = []
fordSales = []

#opens and reads file
with open("Python/PyLab7/carSale.csv","r") as openedFileVar:
	fullList = openedFileVar.readlines()

	for x in fullList[1:8]:
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
		sales.append(listToNums(stringToList[1:9]))
		
	#loop over each sales list to create a new list
	januaryInts = listToNums(janSales)
	februaryInts = listToNums(febSales)
	marchInts = listToNums(marSales)
	aprilInts = listToNums(aprSales)
	mayInts = listToNums(maySales)
	juneInts = listToNums(junSales)
	julyInts = listToNums(julSales)
	augustInts = listToNums(augSales)
	
	#summing the totals
	janTotal = sum(januaryInts)
	febTotal = sum(februaryInts)
	marTotal = sum(marchInts)
	aprTotal = sum(aprilInts)
	mayTotal = sum(mayInts)
	junTotal = sum(juneInts)
	julTotal = sum(julyInts)
	augTotal = sum(augustInts)
	print("\n") 
	print("--- Monthly sales ---")
	print(" The Sum of cars sold in January is",janTotal)
	print(" The Sum of cars sold in February is",febTotal)
	print(" The Sum of cars sold in March is",marTotal)
	print(" The Sum of cars sold in April is",aprTotal)
	print(" The Sum of cars sold in May is",mayTotal)
	print(" The Sum of cars sold in June is",junTotal)
	print(" The Sum of cars sold in July is",julTotal)
	print(" The Sum of cars sold in August is",augTotal)
	print("\n")
	#Working out how to find total yearly sales by manufacturer

	bmwSales =(sales[4])
	vauxhallSales = (sales[3])
	mercSales = (sales[2])
	vwSales = (sales[1])
	fordSales = (sales[0])
		#print(companies)
	

	#summing the totals
	fordTotal = sum(fordSales)
	vwTotal = sum(vwSales)
	mercTotal = sum(mercSales)
	vauxhallTotal = sum(vauxhallSales)
	bmwTotal = sum(bmwSales)
	print("--- Yearly Totals ---")
	print(" The yearly sales total for Ford Motor Company is",fordTotal)
	print(" The yearly sales total for Volkswagen UK is",vwTotal)
	print(" The yearly sales total for Mercedes-Benz UK is",mercTotal)
	print(" The yearly sales total for Vauxhall Motors is",vauxhallTotal)
	print(" The yearly sales total for BMW is",bmwTotal)
	print("\n")
	
	
	
	