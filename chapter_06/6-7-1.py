people = []

person = {"first_name": "zhu", "last_name": "yanbin", "age": 45, "city": "yuzhou"}
people.append(person)

person = {"first_name": "he", "last_name": "tingcan", "age": 46, "city": "xiangxian"}
people.append(person)

person = {"first_name": "xi", "last_name": "jiande", "age": 43, "city": "changge"}
people.append(person)

for person in people:
    name = f'{person['first_name']}{person['last_name']}'
    city = f"{person["city"]}"
    age = f"{person["age"]}"
    print(f'{name}, of {city}, is {age} years old. ')

