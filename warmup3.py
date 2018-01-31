#Matthew Suriawinata        
#1/31/18
#warmup3.py 

num = int(input("Enter a number: "))

if num%2==0 and num%3==0:
    print(num, "is divisable by 2 and 3")
elif num%2==0:
     print(num, "is divisable by 2")
elif num%3==0:
     print(num, "is divisable by 3")
else:
    print(num, "is not divisable by 2 or 3")