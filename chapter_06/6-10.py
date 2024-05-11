favorite_numbers = {
    "mandy": [42, 86, 72],
    "micah": [23, 78, 98],
    "gus": [7, 87, 28],
    "hank": [1_000_000, 9999, 82833983],
    "maggie": [0, 787, 178738],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()} favorite number is:")
    for number in numbers:
        print(f"- { number}")
