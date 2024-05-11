class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1


restaurant = Restaurant("the mean queen", "pizza")


restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(8)
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)
