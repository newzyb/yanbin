cities = {
    "santiago": {
        "country": "chile",
        "population": 6_310_000,
        "nearby mountains": "andes",
    },
    "talkeetna": {
        "country": "united states",
        "population": 876,
        "nearby mountains": "alaska range",
    },
    "kathmandu": {
        "country": "nepal",
        "population": 975_453,
        "nearby mountains": "himilaya",
    },
}

for city, values in cities.items():
    country = values["country"]
    population = values["population"]
    fact = values["nearby mountains"]
    print(f"-{country} about {population} {fact} in -")

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {fact} mounats are nearby.")



