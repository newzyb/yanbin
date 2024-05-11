price = "\nHow old are you?"
price += "\nEnter 'quit', you will end finedish."

while True:
    age = input(price)
    age = int(age)
    if age == "quit":
        break

    if age < 3:
        print(" You are free. ")
    elif age < 12:
        print(" You have pay 10US.")
    else:
        print("You have pay 15Us.")
