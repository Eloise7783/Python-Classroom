print("-----------------------------------------")
print("| Pythagoras' Calculator                |")
print("| 1. Find the length of A given B and C |")
print("| 2. Find the length of B given A and C |")
print("| 3. Find the length of C given A and B |")
print("-----------------------------------------")

calculation = int(input("Please choose calculation 1, 2 or 3:"))

if calculation == 1:
    sideB =(int(input("Enter the value of Side B:")))
    sideC =(int(input("Enter the value of Side C:")))
    sideA=(sideB**2 + sideC**2)
    print(sideA)
if calculation == 2:
    sideA =(int(input("Enter the value of Side A:")))
    sideC =(int(input("Enter the value of Side C:")))
    sideB=(sideA**2 + sideC**2)
    print(sideB)
if calculation == 3:
    sideA =(int(input("Enter the value of Side A:")))
    sideB =(int(input("Enter the value of Side B:")))
    sideC=(sideA**2 + sideB**2)
    print(sideC)