from pathlib import Path
path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/guest_book4.txt")

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_name= []
while True:
    name = input(prompt)
    if name == "quit":
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_name.append(name)

name_string = ""
for name in guest_name:
    name_string += f"{name}\n"
path.write_text(name_string)

