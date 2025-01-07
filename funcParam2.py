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



# Ask the user for 2 integers between 1 and 10
a = int(input("\nPlease input a number between 1 and 10: "))
b = int(input("\nPlease enter a number between 1 and 10: "))

myFunction(a, b)