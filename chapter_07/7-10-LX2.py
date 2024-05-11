name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# 刚开始没有定义字典名，这也就是自己疑惑第13行：places[name] = place 为什么要用列表的方式写出来。
places = {}
while True:
    # 提示输入调查者的名字和回答
    name = input(name_prompt)
    place = input(place_prompt)

    # 将回答存储在字典中
    places[name] = place

    # 是否还有人参与调查
    repeat = input(continue_prompt)
    if repeat == "no":
        break

# 打印出来调查结果
for name, place in places.items():
    print(f"{name} {place}")
