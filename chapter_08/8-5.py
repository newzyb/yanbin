# def describe_city(name="yuzhou", country="China"):
#     print(f"\nI residient {name}, it belong to {country}.")
#     print("Rekjavik is Iceland.")


# describe_city()
# describe_city("xiangxian")
# describe_city("changge", "henan")


def describe_city(city, country="chile"):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city("santiago")
describe_city("reykjavik", "Iceland")
describe_city("punta arenas")
