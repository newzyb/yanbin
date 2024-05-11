favorite_places = {
    "eric": ["bear mountain", "death valley", "tierra del fuego"],
    "erin": ["hawaii", "iceland"],
    "willie": ["mt. verstovia", "the playground", "new hampshire"],
}

for name, places in favorite_places.items():
    # name = favorite_places["name"]
    print(f"\n{name.title()} likes the following places: ")

    for place in places:
        print(f"-{place.title()}")
