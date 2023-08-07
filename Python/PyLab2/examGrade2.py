level = int(input("please enter the exam level: "))
grade = int(input("please enter the number of points: "))
if grade <1 or grade >100:
    print("Error: marks must be between 1 and 100")

if(level == 1):
    if grade <50:
        print("Fail")
    elif grade >=50 or grade <=60:
        print("Pass")
    elif grade >=61 or grade <=70:
        print("Merit")
    elif grade >=71 or grade <=100:
        print("Distinction")
if(level == 2):
    if grade <40:
        print("Fail")
    elif grade >=40 or grade <=50:
        print("Pass")
    elif grade >=51 or grade <=65:
        print("Merit")
    elif grade >=66 or grade <=100:
        print("Distinction")