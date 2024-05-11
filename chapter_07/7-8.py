sandwich_orders = ["American", "Italin", "france"]
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print(f"\nVerifying user: {finished_sandwiche}")

    print(f"I made your tuna sandwich - {finished_sandwiche}.")

    finished_sandwiches.append(finished_sandwiche)
    print("\nVerifying  you made a new list: ")
for finished_sandwiche in finished_sandwiches:
    print(f"{finished_sandwiche}")
