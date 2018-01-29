#Matthew Suriawinata
#1/29/18
#unitConverter.py


print("1) Kilometer to Miles")
print("2) Kilograms to Pounds")
print("3) Liters to Gallons")
print("4) Celsius to Fahrenheit")




option = int(input("Choose a number: "))


if option == 1: 
    num = int(input("Enter Kilometers: "))
    print(num, "kilometers is", 0.621371*num, "miles")
    
elif option == 2:
    num = int(input("Enter Kilograms: "))
        print(num, "kilograms is", 2.2*num, "pounds")
        
elif option == 3:
    num = int(input("Enter Liters: "))
        print(num, "Liters is", 0.264172*num, "gallons")
else:
    num = int(input("Enter Celsius: "))
        print(num, "Celsius is", (9/5)*num + 32, "Fahrenheit")
