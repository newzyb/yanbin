name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

polling_active = True

while polling_active:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} you visit place {place}.")
