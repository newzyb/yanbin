def make_album(artist, album):
    full_name = f"{artist}, {album}"
    return full_name.title()


album = make_album("zhangxueyou", "wenbie")
print(album)
album = make_album("liudehua", "wangqingshui")
print(album)
album = make_album("duiniaibuwan", "guofucheng")
print(album)
