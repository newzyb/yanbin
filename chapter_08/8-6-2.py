def city_country(first, last):
    full_name = f"{first} {last}"
    return full_name.title()


cc = city_country("santiago", "chile")
print(cc)
cc = city_country("henan", "china")
print(cc)
cc = city_country("jiangsu", "china")
print(cc)
