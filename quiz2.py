#Matthew Suriawinata
#2/12/18
#quiz2.py


word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

if len(word2) == len(word1):
    print("The words are the same length")
elif len(word2) > len(word1):
    print(word2, "is longer than ", word1)
elif len(word1) > len(word2):
    print(word1, "is longer than ", word2)
    

if "p" in word2 and "p" in word1:
    print("Both words have a p")
elif "p" in word2:
    print(word2," has a p")
elif "p" in word1:
    print(word1," has a p")
    
    
print("Enter two numbers that add up to 12 ")

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if (num1 + num2) == 12:
    print("Correct")
else:
    print("Incorrect")
    
 
