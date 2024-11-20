print(" Title: stageOfLife.py ")
print("")
print("~~~~~~ Questions ~~~~~~") 
print("")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print("")
print("****** RESULTS ******")
print("")
print("Hello", name)

if age >= 8 and age <= 12:
    print("You are currently in the childhood stage of your life")
elif age >= 13 and age <= 19:
    print("You are currently in the teenager stage of your life")
elif age >= 20 and age <= 29:
    print("You are currently in the young adult stage of your life")
elif age >= 30 and age <= 55:
    print("You are currently in the adult stage of your life")
elif age >= 56 and age <= 65:
    print("You are currently in the wise person stage of your life")
elif age >= 66 and age <= 100:
    print("You are currently in the retirement stage of your life")
else:
    print("Please input valid data")
    

    
    
