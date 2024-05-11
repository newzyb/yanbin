sandwich_orders = [
    "veggie",
    "pastrami",
    "grilled cheese",
    "pastrami",
    "turkey",
    "roast beef",
    "pastrami",
]

# 这个写法是错误的，造成了无限循环。
while sandwich_orders:
    # sandwich_orders.remove("pastrami")
    print(sandwich_orders)
