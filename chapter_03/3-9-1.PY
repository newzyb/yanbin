cars = ["bmw", "audi", "toyota", "subaru"]

print(sorted(cars))

print(sorted(cars, reverse=True))

cars.reverse()
print(cars)

print(len(cars))

print(cars[1].title())

cars[1] = "benz"
print(cars)

cars.append("dazhong")
print(cars)

cars.insert(3, "wuling")
print(cars)

del cars[4]
print(cars)

popped_cars = cars.pop(4)
print(popped_cars)
print(f"I buy first motorcycle is {popped_cars}.")

cars.remove("wuling")
print(cars)
