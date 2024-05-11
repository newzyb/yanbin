favorite_places = {
    "hetingcan": ["shanghai", "beijing", "nanjing"],
    "xijiande": ["shandong", "hebei", "qinhuangdao"],
    "limingxin": ["beijing", "henan", "heilongjiang"],
}

for place, points in favorite_places.items():
    print(f"\n{place} favorite places is :")
    for point in points:
        print(f"- {point}")
