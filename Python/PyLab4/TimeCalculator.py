print("-------------------------------------------")
print("| Time Calculator                         |")
print("| 1 - Add 2 times                         |")
print("| 2 - Find the difference between 2 times |")
print("| 3 - Convert to Hours                    |")
print("| 4 - Convert to Minutes                  |")
print("| 5 - Convert Minutes to Time             |")
print("| 6 - Convert Hours to Time               |")
print("| 7 - Convert Days to Time                |")
print("| 8 - Exit                                |")
print("-------------------------------------------")

option = int(input("Enter an option: "))
while option != 9:
    if option == 1:
        dayTimeStr1 = input("Enter the first time, DD:HH:MM -")
        dayTimeStr2 = input("Enter the second time, DD:HH:MM -")
        #making the list
        listOfTimes1 = dayTimeStr1.split(':')
        listOfTimes2 = dayTimeStr2.split(':')
        #picking the individual elements for first time
        dayOfMonth1 = int(listOfTimes1[0])
        hourOfDay1 = int(listOfTimes1[1])
        minuteOfDay1 = int(listOfTimes1[2])
        #picking the individual elements for second time
        dayOfMonth2 = int(listOfTimes2[0])
        hourOfDay2 = int(listOfTimes2[1])
        minuteOfDay2 = int(listOfTimes2[2])
        #adding the minutes
        addedMinutes = minuteOfDay1 + minuteOfDay2
        #adding the hours
    elif option == 2:
        dayTimeStr1 = input("Enter the first time, DD:HH:MM -")
        dayTimeStr2 = input("Enter the second time, DD:HH:MM -")
    elif option == 3:
        dayTimeStr = input("Enter the time you wish to convert, DD:HH:MM -")
    elif option == 4:
        dayTimeStr = input("Enter the time you wish to convert, DD:HH:MM -")
    elif option == 5:
        dayTimeStr = input("Enter the time you wish to convert, DD:HH:MM -")
    elif option == 6:
        dayTimeStr = input("Enter the number of hours you wish to convert, HH -")
    elif option == 7:
        dayTimeStr = input("Enter the number of days you wish to convert, DD -")
    elif option == 8:
        break