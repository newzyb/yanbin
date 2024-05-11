from pathlib import Path
import json

path= Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/favorite_number.json")
try:
    conutents=path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    conutents= json.dumps(number)
    path.write_text(conutents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(conutents)
    print(f"I know your favorite number! It's {number}.")