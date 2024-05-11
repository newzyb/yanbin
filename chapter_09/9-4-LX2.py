class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} sever {self.type}.\n"
        print(msg)

    def open_restaurant(self):
        msg = f"{self.name} is open.\n"
        print(msg)

    # 第二种修改默认值的方式
    def served_number(self, number):
        self.number_served = number
        print(f"-----This restaurant had served {self.number_served}\n")

    def set_number_served(self):
        print(f"{self.number_served}")


restaurant = Restaurant("The mean queen", "Pizza")
# print(restaurant.name)
# print(restaurant.type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()


restaurant.served_number(88)

# restaurant.set_number_served()
