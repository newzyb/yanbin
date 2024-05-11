from pathlib import Path
import json

def get_stored_name(path):
    if path.exists():
        contents = path.read_text()
        user_dict=json.loads(contents)
        return user_dict
    else:
        return None

def get_new_name(path):
    username= input("What is your name? ")
    game = input("What's your favorite game? ")
    animal =input("What's your favorite animal? ")

    user_dict={"username": username, "game": game, "animal": animal,}
    countents = json.dumps(user_dict)
    path.write_text(countents)
    return user_dict

def greet_user():
    path= Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/user_info.json")
    user_dict = get_stored_name(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict= get_new_name(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()


