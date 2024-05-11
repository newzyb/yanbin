from pathlib import Path

path = Path("H:/Visual Studio Code/Python-3-ZYB/chapter_10/guest.txt")

msg = input("Plese input you name.")
path.write_text(msg)
