'''
Author:Eva Donahue
Program: forLoops.py
Last Update: 9/25/2024
Sample for Loop Statement
'''

for blah in range(5):
    print("blah blah", end ="") # empty string to create a blank space

print("This print statment is outside of our for Loop.")

print() # Empty print statements will create a blank line
print() #works like <br> in html
print()
'''
Using Outside Variables in a for Loop
'''
print("Using Outside Variables in a for Loop")
print("--------------------------------")
number = 5
exponent = 4
product = 1

# Create a for loop to find the value of our number to the exponent
for eachPass in range(exponent): 
    product = product * number
    print(product, end=" ")
print("\n") # \n is a character to create a New Line <br>

print(product) #625

print("\n\n\nCount-Controlled Loops")
print("--------------------------\n\n")

for count in range(4):
    print(count, end=" - ")
print()

print("Off-by-one error occurs because by defailt counting always starts at 0")

print("\nOff-by-one correction")
print("------------------------\n")
product = 1 

for count in range(4): 
    product = product * (count + 1)
print(product)


print("\n\nUsing Lower & Upper Bounds")
print("------------------------------")

product = 1 

for count in range (1, 5):
    product = product * count 

print(product)

print("\n\n Summation using Lower & Upper Bounds")
print("----------------------------------\n\n")

lower = int(input("Enter the Lower Bound: "))
upper = int(input("Enter the Upper Bound: "))

theSum = 0 

for number in range(lower, upper + 1):
    theSum = theSum + number

print("The summation of the numbers between", lower ,  "and", upper, "is equal to:", theSum)