def make_album(artist, title):
    album = f"{artist}, {title}"
    return album


while True:
    print("Please tell me your name:")
    print("Enter 'quit' at any time to quit.")

    art = input("artist name: ")
    tit = input("title name: ")
    if art == "quit" or tit == "quit":
        break
    full_name = make_album(art, tit)
    print(f"Hello, {full_name}")
