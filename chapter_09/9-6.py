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
    def __init__(self, name, cuisine_type="ice cream") -> None:
        super().__init__(name, cuisine_type)
        self.flavors = []
        pass

    def show_flavor(self):
        for flavor in self.flavors:
            print(f"{flavor}.")


restaurant = Restaurant("the mean queen", "pizza")
# print(restaurant.name)
# print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

icecream = IceCreamStand("Big one")
icecream.flavors = ["lanmei", "caomei", "black cherry"]

icecream.describe_restaurant()
icecream.show_flavor()
