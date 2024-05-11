def make_album(artist, title):
    album = f"{artist}, {title}"
    return album


while True:
    first = print("Please tell me your name:")
    last = print("enter 'quit' at any time to quit.")

    art = input(first)
    tit = input(last)
    if art == "quit" or tit == "quit":
        break
full_name = make_album(art, tit)
print(full_name)
# 并没有窗口互动，提示自己在哪里输入，只是把上面print的内容给打印出来了。
