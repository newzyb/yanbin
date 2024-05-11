def city_country(city, country):
    return f"{city.title()}, {country.title()}."


city = city_country("yuzhou", "henan")
print(city)

city = city_country("changge", "xuchang")
print(city)

city = city_country("santiago", "chile")
print(city)
