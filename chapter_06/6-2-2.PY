favorite_numbers = {
    "hetingcan": 6,
    "limingxin": 8,
    "zhangchao": 9,
    "wupengju": 10,
    "zhuyanbin": 888,
}

for name in favorite_numbers:
    print(name.title())
for point in favorite_numbers.values():
    print(point)

for key, value in favorite_numbers.items():
    print(f"\nname: {key.title()}")
    print(f"point: {value}")

for name in set(favorite_numbers):
    print(name)

for point in set(favorite_numbers.values()):
    print(point)
