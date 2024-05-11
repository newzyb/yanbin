# 使用if的用法，写出来并不是一个字典类型的python.
def make_album(artist, album, number=None):

    if number:
        full_name = f"{artist}, {album}, {number}"
    else:
        full_name = f"{artist}, {album}"
    return full_name.title()


album = make_album("zhangxueyou", "wenbie", "18")
print(album)
album = make_album("liudehua", "wangqingshui", "9")
print(album)
album = make_album("duiniaibuwan", "guofucheng")
print(album)
