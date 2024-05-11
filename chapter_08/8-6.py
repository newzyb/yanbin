def city_country(city, country):
    dounber_name = f"{city}, {country}."
    return dounber_name.title()


fullName = city_country("yuzhou", "henan")
print(fullName)

fullName = city_country("hangzhou", "zhejiang")
print(fullName)

fullName = city_country("santiago", "chile")
print(fullName)
