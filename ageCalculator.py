#Matthew Suriawinata
#2/5/18
#ageCalculator.py - calculates your age


from datetime import date

year = int(input("Enter the year you were born in: "))
month = int(input("Enter the month you were born in: "))
day = int(input("Enter the day you were born on: "))

if month > 12 or day > 31:
    print("Start again, and enter a date")
else:
    yearNow = date.today().year
    monthNow = date.today().month
    dayNow = date.today().day

    if monthNow < month:
        print("You are", yearNow - year - 1, "years old")
    elif monthNow == month:
        if dayNow < day:
            print("You are", yearNow - year - 1, "years old")
        else:
            print("You are", yearNow - year, "years old")
    else:
        print("You are", yearNow - year, "years old")
        
        
    
