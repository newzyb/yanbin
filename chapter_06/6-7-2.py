# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    "first_name": "eric",
    "last_name": "matthes",
    "age": 46,
    "city": "sitka",
}
people.append(person)

person = {
    "first_name": "lemmy",
    "last_name": "matthes",
    "age": 2,
    "city": "sitka",
}
people.append(person)

person = {
    "first_name": "willie",
    "last_name": "matthes",
    "age": 11,
    "city": "sitka",
}
people.append(person)

for person in people:
    name = f"{person['first_name']}{person['last_name']}"
    print(f"\n{name.title()} \n")

    for key, value in person.items():
        print(f"{key}: {value}")

    age = person["age"]
    city = person["city"]
    print(f"\n{name}, of {city},is {age} years old.")
