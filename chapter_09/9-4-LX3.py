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

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"{self.number_served}")

    def increment_number_served(self, number_served):
        self.number_served += number_served


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(3500)
restaurant.set_number_served()

restaurant.increment_number_served(18)
restaurant.set_number_served()
