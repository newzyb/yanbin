class Restaurant:
    # 第一种修改属性值的方法：
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

    def set_number_served(self):
        print(f"{self.number_served}")


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 第一种修改属性值的方式
restaurant.number_served = 34

# restaurant.served_number()
restaurant.set_number_served()
