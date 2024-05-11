from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents= path.read_text()
        username= json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username= input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/username.json")
    username= get_stored_username(path)
    if username:
        correct=input(f"Are you {username}? (y/n) ")
        if correct == "y":
            print(f"Welcome back, {username}!")
        else:
            username=get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username=get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
greet_user()




