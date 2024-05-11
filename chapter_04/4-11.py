pizzas = ["italy", "france", "germany", "america"]
friend_pizzas = pizzas[:]

pizzas.insert(2, "china")
print(pizzas)

friend_pizzas.append("iceland")
print(friend_pizzas)

print(f"My favorite pizzas are:{pizzas}.")

for pizza in pizzas:
    print(pizza)

print(f"My friend's favorite pizzas art: {friend_pizzas}.")

for friend_pizza in friend_pizzas:
    print(friend_pizza)
