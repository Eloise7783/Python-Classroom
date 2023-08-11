mark1 = int(input('Input Maths mark: '))
mark2 = int(input('Input English mark: '))
mark3 = int(input('Input ICT mark: '))

marks = [mark1, mark2, mark3]

markAverage = mark1 + mark2 + mark3 / 3
totalMarks = mark1 + mark2 + mark3

for mark in marks:
    if mark1 > 100:
        print("Invalid mark, please input a score between 0 and 100")
    elif mark2 > 100:
        print("Invalid mark, please input a score between 0 and 100")
    elif mark3 > 100:
        print("Invalid mark, please input a score between 0 and 100")

if markAverage >= 65:
   print("pass")
   print("Total mark is:", totalMarks)
   print("Mark Average is:", markAverage)
elif markAverage < 65:
   print("fail")
   print("Total mark is:", totalMarks)
   print("Mark Average is:", markAverage)