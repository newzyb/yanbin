# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    "animal type": "python",
    "name": "john",
    "owner": "guido",
    "weight": 43,
    "eats": "bugs",
}
pets.append(pet)

pet = {
    "animal type": "chicken",
    "name": "clarence",
    "owner": "tiffany",
    "weight": 2,
    "eats": "seeds",
}
pets.append(pet)

pet = {
    "animal type": "dog",
    "name": "peso",
    "owner": "eric",
    "weight": 37,
    "eats": "shoes",
}
pets.append(pet)

for pet in pets:
    print(f"{pet['name'].title()}")
    type = pet["animal type"]
    owner = pet["owner"]
    weight = pet["weight"]
    eats = pet["eats"]
    for key, value in pet.items():
        print(f"{type}, {owner}, {weight}, {eats}")
