prompt = "Tell me something, and I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program. " 

message = input(prompt)

while message != 'quit':
    message = input(prompt)
    print(message)