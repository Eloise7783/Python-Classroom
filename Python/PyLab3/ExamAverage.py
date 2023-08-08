mark1 = int(input('Input Maths mark: '))
mark2 = int(input('Input English mark: '))
mark3 = int(input('Input ICT mark: '))

markAverage = mark1 + mark2 + mark3 / 3

if markAverage >= 65:
    print("pass")
elif markAverage < 65:
    print("fail")