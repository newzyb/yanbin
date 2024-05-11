rivers = {
    "nile": "egypt",
    "huanghe": "china",
    "mississippi": "united states",
    "fraser": "canada",
    "yangtze": "china",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)
