favorite_places = {
    "hetingcan": {"city1": "shanghai", "city2": "beijing", "city3": "nanjing"},
    "xijiande": {"city1": "shandong", "city2": "hebei", "city3": "qinhuangdao"},
    "limingxin": {"city1": "beijing", "city2": "henan", "city3": "heilongjiang"},
}

for name, citys in favorite_places.items():
    c1 = citys["city1"]
    c2 = citys["city2"]
    c3 = citys["city3"]
    print(f"\n{name.title()} favorite city is: ")
    print(f"--{c1}")
    print(f"--{c2}")
    print(f"--{c3}")
