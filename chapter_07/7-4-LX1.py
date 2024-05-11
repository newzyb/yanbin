pizza = "\nWhat topping would you like on your pizza?"
pizza += "\nEnter 'quit' when you are finished:"


while True:
    topping = input(pizza)
    if topping != "quit":
        print(f"Would you like {topping}?")
    else:
        break

# 两种不同的写法，显示的结果是相同的。
while True:
    topping = input(pizza)
    if topping == "quit":
        break
    else:
        print(f"Would you like {topping}?")
