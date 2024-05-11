price = "\nHow old are you?"
price += "\nEnter 'quit', you will end finedish."
age = input(price)
age = int(age)

while age != "quit":

    if age < 3:
        print(f"{age}You are free  ")
    else:
        print(age)
