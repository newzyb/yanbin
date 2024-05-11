from pathlib import Path

path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/guest_book3.txt")
msg = "\nHi, what's your name? "
msg += "\nEnter 'quit' if you're the last guest."

guest_name = []
while True:
    name = input(msg)
    if name == "quit":
        break
    print(f"Thank {name}, we'll add you to the guest book.")
    guest_name.append(name)

first_string = ""
for name in guest_name:
    first_string += f"{name}\n"
path.write_text(first_string)
