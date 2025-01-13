def doubleNumber(x):
    doubled_x  = 2 * x
   # print(doubled_x)
    return doubled_x

num_apples = 4
print("Before: " + str(num_apples))

twice_as_many = doubleNumber(num_apples) #the function will return doubled_x here and replace doubleNumber(num_apples) with whatever the return value is
print("After: " + str(twice_as_many))

y=11
print(doubleNumber(y))

print("\nSquare with Return Values Example(my code from codehs)")
print("---------------------------------------\n")

# Enter your code here
#function that squares number
def square(x):
    squared = x * x
    return squared
    
#squares 5
y = square(5)
print(y)

#squares 6
num=square(6)
print(num)
