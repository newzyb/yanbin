class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} sever {self.type}."
        print(msg)

    def open_restaurant(self):
        msg = f"{self.name} is open."
        print(msg)

    def served_number(self):
        print(f"This restaurant had served {self.number_served}")

    def set_number_served(self):
        print(f"{self.number_served}")

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 34

restaurant.served_number()
restaurant.set_number_served()

# restaurant.increment_number_served(2)
# restaurant.number_served()
