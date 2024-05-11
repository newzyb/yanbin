sandwich_orders = ["American", "Italin", "france"]
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print(f"Verifying user: {finished_sandwiche}")
    finished_sandwiches.append(finished_sandwiche)
    print(f"\nI made your tuna sandwich{finished_sandwiche}.")
# 打错了\n符号，造成分隔行差开了一行，就不能理解其中的意思了。
