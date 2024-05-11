class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        pass

    def describe_restaurant(self):
        print(f"My restaurant name is {self.name}.")
        print(f"cuisine type is {self.type}.")

    def open_restaurant(self):
        msg = f"{self.name} is open."
        print(msg)


My_restaurant = Restaurant("yanbin", "CHina")
print(f"My restaurant name is {My_restaurant.name}.")
print(f"cuisine type is {My_restaurant.type}.")
# print(f"{open_restaurant.name} is open.")
My_restaurant.open_restaurant()
My_restaurant.describe_restaurant()
