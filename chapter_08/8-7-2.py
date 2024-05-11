def make_album(singer, album, number=None):
    album_dict = {
        "singer": singer.title(),
        "album": album.title(),
    }
    return album_dict


# 没有写if语句，把字典中的扩展项（可选形参值）打印出来。

album = make_album("zhangxueyou", "wenbie", number=1)
print(album)
album = make_album("liudehua", "wangqingshui")
print(album)
album = make_album("guofucheng", "woduiniaibuwan")
print(album)
