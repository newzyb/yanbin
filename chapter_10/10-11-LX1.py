from pathlib import Path
import json

number =input("What's your favorite number? ")

path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/favorite_number.json")
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")

