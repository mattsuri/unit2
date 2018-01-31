#Matthew Suriawinata    
#1/30/18
#slope.py - slopes

x1 = int(input("x1 = "))

y1 = int(input("y1 = "))

x2 = int(input("x2 ="))

y2 = int(input("y2 ="))

slope = (y1 - y2 )/(x1 - x2)

yintercept = y1 - (slope * x1) 

if x1-x2 == 0:
    print("Your slope is undefined")
    print("The equation of the line is x = ", x1)
else:
    print("Your slope is ", slope)
    print("Your equation is y = ", slope, "x +", yintercept)

