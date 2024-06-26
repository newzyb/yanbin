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

for name, city_info in cities.items():
    country = city_info["country"]
    population = city_info["population"]
    mountain = city_info["nearby mountains"]
    print(f"\n{name.title()} is in {country}: ")
    print(f"It has a population of about {population}")
    print(f"The{mountain} mounats are nearby.")
