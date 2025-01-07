'''
This program will accept 2 inputs from the user and process the data as exponents of one another.
'''
# This functions prints the 2 user inputs and then calculates them as exponents of one another and prints them out to the terminal
def myFunction(a , b):
    print("\nVariable a is: ", a,".")
    print("\nVariable a is: ", b,".")
    exp1 = a ** b
    exp2 = b ** a 
    print("\n", a, "to the power of ", b, "is: ", exp1)
    print("\n", b, "to the power of ", a, "is: ", exp1)

def sum(first, second):
    total = first + second
    print("The total of your data input is:", total)

# Ask the user for 2 integers between 1 and 10
a = int(input("\nPlease input a number between 1 and 10: "))
b = int(input("\nPlease enter a number between 1 and 10: "))

myFunction(a, b)


print("\n Part 2 of our Example:\n")


#Give the user the option to repeat this process as many times as they want.
#If they want to quit, they type the word Quit
    # Have users input positive integers
myVar1 = int(input("Please Enter a positive whole number or type Quit to exit"))
myVar2 = int(input("Please Enter a positive whole number "))

# call the sum() function to 
sum(myVar1, myVar2)