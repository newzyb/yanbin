favorite_places = {
    "hetingcan": {"city": "shanghai", "city": "beijing", "city": "nanjing"},
    "xijiande": {"city": "shandong", "city": "hebei", "city": "qinhuangdao"},
    "limingxin": {"city": "beijing", "city": "henan", "city": "heilongjiang"},
}

for place in favorite_places:
    print(f"{place.title()} favorite city is :")
    # name = place["city"]
    # 以为可以在字典里面设置for循环，结果，这样做不正确。
    # 正确的设置方法见6-9-2.py
    for country, point in place.items():
        print(f"{country}: {point}.")
