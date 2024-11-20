color = input("What is your favorite color?: ").lower.strip
print("Animals: Dog, Cat, Lion, Tiger, Rabbit, Bird, Dolphin, Elephant, Sloth, Turtle")
animal = input("What is your favorite animal from the list?: ")


print("Your favorite color is", color, "and your favorite animal is", animal, "interesting... hm...")

if animal == "dog" or animal == "cat":
    print("From what you've input, you are a gentle and open-minded")
elif animal == "lion" or animal == "tiger":
    print("From what you've input, you are extroverted and ambitious")
elif animal == "rabbit" or animal == "bird":
    print("From what you've input, you are soft-spoken and calm")
elif animal == "sloth" or animal == "turtle":
    print("From what you've input, you are introverted and can be hesitant to try new things")
else: 
    print("Please input valid data!")
