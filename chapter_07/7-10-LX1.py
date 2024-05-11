name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# 虽然是明白了把两个需要客户输入的信息变成字典，但是，清晰的定义两条信息，让机器没有错误的读下来，也是非常重要的。
# 没有首先定义字典名

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    responses[name] = place

    repeat = input(continue_prompt)
    if repeat == "no":
        break
for name, place in responses.items():
    print(f"{name} {responses}")
