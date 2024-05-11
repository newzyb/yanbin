sandwich_orders = [
    "veggie",
    "pastrami",
    "grilled cheese",
    "pastrami",
    "turkey",
    "roast beef",
    "pastrami",
]

print("Sorry, pastrami had sell out.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(f"\n{sandwich_orders}")
