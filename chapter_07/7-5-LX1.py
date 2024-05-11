price = "\nHow old are you?"
price += "\nEnter 'quit', you will end finedish."
age = input(price)
age = int(age)

# 这是一个错误的写法：如果while循环条件写成age != 'quit',就会导致程序不断循环。
while age != "quit":

    # 这个if语句并没有搞清楚三个条件之间的关系，写的比较混乱。
    if age < 3:
        print(f"You are free  ")
    elif age > 3 and age < 12:
        print(f"{age} You have pay 10US  ")
    elif age > 12:
        print(f"{age} You have pay 15Us. .")
    else:
        print("You are free.")
