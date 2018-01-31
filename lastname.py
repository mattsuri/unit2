#Matthew Suriawinata
#1/31/18
#lastname.py - tells whether last name is in the first or second half of the alaphabet

last_name = input("Enter your last name: ")
lastName = last_name.lower()
if lastName > "a" and lastName < "m":
    print("Your name is in the first half of the alphabet")
else:
    print("Your name is the the second half of the alphabet")

