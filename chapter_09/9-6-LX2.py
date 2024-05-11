class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def flavor(self):
        for flavor in self.flavors:
            print(f"- {flavor}")


# restaurant = Restaurant("the mean queen", "pizza")


big_one = IceCreamStand("big one", "ice cream")
big_one.flavors = ["vanilla", "chocolate", "black cherry"]

big_one.describe_restaurant()
big_one.flavor()
