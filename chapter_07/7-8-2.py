sandwich_orders = ["veggie", "grilled cheese", "turkey", "roast beef"]
finished_sanwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"verifying :{sandwich}")
    finished_sanwiches.append(sandwich)
print(finished_sanwiches)
for finished_sanwiche in finished_sanwiches:
    print(finished_sanwiche)
