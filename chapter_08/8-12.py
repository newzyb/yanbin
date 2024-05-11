def make_sandwich(*toppings):
    print(toppings)


def make_pizza(size, *toppings):
    print(f"Making a {size} -inch pizze with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich("djkfl")
make_sandwich("djfklae", "klfjdoie")
make_sandwich("ijepj", "dfklae", "jdfklaei")

make_pizza(16, "pepperoni")
make_pizza(12, "mushroons", "green peppers", "extra cheese")
