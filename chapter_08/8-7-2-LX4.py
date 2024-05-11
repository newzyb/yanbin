# 使用字典类型，写出来python语句。
def make_album(artist, title, num_songs=0):
    artist_album = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if num_songs:
        artist_album["num_songs"] = num_songs
    return artist


# 在return语句中只写了artist,导致下面输出显示的只有字典中artist中的内容，没有把剩下的两项内容（title, num_songs) 完全输出。
# 在return中错误返回了字段，没有写全，导致输出不完整。
album = make_album("zhangxueyou", "wenbie", "18")
print(album)
album = make_album("liudehua", "wangqingshui", "9")
print(album)
album = make_album("duiniaibuwan", "guofucheng")
print(album)
