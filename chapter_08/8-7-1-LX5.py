def make_album(artist, titile):
    artist_album = {
        "artist": name,
        "title": title,
    }
    return artist_album


# 定义字典时，没有搞清楚变量是谁。

msg = make_album("zhangxueyou", "wenbie")
print(msg)
