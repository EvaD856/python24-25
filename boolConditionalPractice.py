print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero
number = -3

# Write an if/else (elif) structure to determine the number's positive, negative, zero state

if number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("Error: Data is invalid")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = "admin"

# Write your Code Below
if user_role == "admin":
    print("You have admin privleges.")
else: 
    print("You do not have admin privleges.")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
year = 2024

# Write your Code Below

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year.")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = 25

# Write your Code Below
if age == 0: 
    print("Age Group: Newborn ")
elif age < 5 and age > 0:
    print("Age Group: Toddler ")
elif age >= 5 and age < 13:
    print("Age Group: Child")
elif age >= 13 and age < 18:
    print("Age Group: Teenger")
elif age >= 18 and age < 30: 
    print("Age Group: Young Adult")
elif age < 65 and age >= 30:
    print("Age Group: Adult")
elif age >= 65:
    print("Age Group: Elderly")
else:
    print("Error: You put in invalid data")



print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = 120

# Write your code Below

if purchase_amount < 50 and purchase_amount >= 25:
    print("You get a 5% discount because you spent $25!!")

elif purchase_amount <100 and purchase_amount >= 50:
    print("You get a 10% discount because you spent $50 or more!!")

elif purchase_amount >= 100 and purchase_amount < 1000:
    print("You get a 15% discount because you spent $100 or more!!")

elif purchase_amount >= 1000:
    print("You get a 10% discount because you spent ONE THOUSAND DOLLARS or more!!!!!")
else:
    print("You do not get a discount. Please spend more!!")
