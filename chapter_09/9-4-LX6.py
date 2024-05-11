class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(msg)

    def open_restaurant(self):
        msg = f"{self.name} is open, come in."
        print(msg)

    def served_number(self):
        print(self.number_served)

    # 通过方法修改属性值(二)
    def default_number(self, number):
        self.number_served = number


restaurant = Restaurant("the mean queen", "pizza")

restaurant.describe_restaurant()
restaurant.open_restaurant()
# 直接修改属性默认值（一）
restaurant.number_served = 99
restaurant.served_number()

restaurant.default_number(888)
# restaurant.served_number()
