#Matthew Suriawinata    
#1/30/18
#slope.py - slopes

x1 = int(input("x1 = "))

y1 = int(input("y1 = "))

x2 = int(input("x2 ="))

y2 = int(input("y2 ="))





if x1-x2 == 0:
    print("The slope is undefined")
    print("The equation of the line is x = ", x1)
else:
    slope = (y1 - y2 )/(x1 - x2)
    yintercept = y1 - (slope * x1) 
    print("The slope is ", slope)
    print("The equation is y = ", slope, "x +", yintercept)

