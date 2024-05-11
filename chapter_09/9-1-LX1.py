class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} sever {self.type}."
        print(msg)

    def open_restaurant(self):
        msg = f"{self.name} is open."
        print(msg)


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
