# def describe_city(city, country="china"):
#     msg = f"i am come from {city}, it is belong in {country}."
#     print(msg)


# describe_city("yuzhou")
# describe_city("yanling", "henan")
# describe_city("reykjavik", "Iceland")


def describe_city(city, country="chile"):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city("yuzhou")
describe_city("changge")
describe_city("Reykjavik", "Iceland")
