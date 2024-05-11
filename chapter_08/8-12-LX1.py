def make_sandwich(*items):
    print("\nPlease you idented items: ")
    for item in items:
        print(f"---{item}")


make_sandwich("roast beef", "cheddar cheese", "lettuce", "honey dijon")
make_sandwich("turkey", "apple slices", "honey mustard")
make_sandwich("peanut butter", "strawberry jam")
