age = "How many you age?"

while True:
    price = input(age)
    price = int(price)
    if price == "quit":
        break

    if price < 3:
        print(f"{price}, you are free.")
    elif price < 12:
        print(f"{price},you will pay 10Us.")
    else:
        print("you will pay 15Us.")
