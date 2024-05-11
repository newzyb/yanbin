# 使用字典类型，写出来python语句。
def make_album(artist, title, num_songs=0):
    artist_album = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if num_songs:
        artist_album["num_songs"] = num_songs
    return artist_album


album = make_album("zhangxueyou", "wenbie", "18")
print(album)
album = make_album("liudehua", "wangqingshui", "9")
print(album)
album = make_album("duiniaibuwan", "guofucheng")
print(album)
