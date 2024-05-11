pizza = "please you input: "
while True:
    topping = input(pizza)

    if topping == "quit":
        break
    else:
        print(f"I'd love this {topping}.")
