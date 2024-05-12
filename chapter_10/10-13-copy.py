from pathlib import Path
import json

# 函数get_stored_name的目的是从给定路径读取文本内容，并将其作为JSON解析成字典
# 在使用这个函数时，你需要提供一个文件路径，这个路径可以是一个字符串或者一个Path对象。
# 如果指定的文件存在，函数会读取内容，解析JSON，然后返回一个字典。
# 如果文件不存在，可以选择返回None或者抛出一个FileNotFoundError异常。
def get_stored_name(path):
    # 检查文件路径是否存在
    if path.exists():
        # 读取文件中的文本内容
        contents = path.read_text()
        # 将读取的内容从 JSON 字符串转换成 Python 字典
        user_dict =json.loads(contents)
        # 返回这个字典
        return user_dict
    else:
        return None

# 代码示例中定义了一个 get_new_name 函数，该函数从用户那里获取输入并保存到一个字典中，然后将该字典以 JSON 格式写入到给定的文件路径中。
def get_new_name(path):
    # 从用户那里获取信息
    username= input("What is your name? ")
    game = input("What's your favorite game? ")
    animal =input("What's your favorite animal? ")
    
    # 将信息保存到字典中
    user_dict={"username": username, "game": game, "animal": animal,}
    # 将字典转换为 JSON 格式的字符串
    countents = json.dumps(user_dict)
    # 将 JSON 字符串写入到指定的文件路径
    path.write_text(countents)
    # 返回用户信息字典
    return user_dict  # 返回用户信息的字典，已经保存到文件中
# 在这段代码中，函数 get_new_name 首先提示用户输入名字、最喜欢的游戏和动物，然后创建一个包含这些信息的字典。
# 之后，它将字典转换为 JSON 格式的字符串，并将这个字符串写入到指定的文件路径。最后，函数返回这个用户信息字典。


# 在 greet_user 函数中，从一个 JSON 文件中检索用户信息，并打印一条问候消息。
# 如果用户信息不存在，则提示用户输入新的信息，并保存它们。
def greet_user():
    # 定义要访问的用户信息文件的路径
    path= Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/user_info.json")
    # 从 JSON 文件中获取存储的用户信息
    user_dict = get_stored_name(path)

     # 如果用户信息存在，打印欢迎消息
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        # 如果用户信息不存在，提示用户输入新的信息，并保存
        user_dict= get_new_name(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

# 在这个函数中，如果用户信息已经保存在 JSON 文件中，则会打印一条问候消息。
# 如果 JSON 文件不存在或者是空的，将会提示用户输入名字、最喜欢的游戏和最喜欢的动物，并保存这些信息到 JSON 文件中。
# 然后，打印一条消息告诉用户，他们的信息将被记住。

# 调用 greet_user 函数
greet_user()



