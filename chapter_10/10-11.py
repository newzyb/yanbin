from pathlib import Path
import json


path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/favorite_number.json")
contents = path.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}.")
