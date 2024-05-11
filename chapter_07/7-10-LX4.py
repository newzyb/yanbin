name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    if name == "quit":
        break
    place = input(place_prompt)
    if place == "quit":
        break
    responses[name] = place
for name, place in responses.items():
    print(f"{name}, {place}")
# if语句只用一个就行，回答为：yes/no退出。
