def make_car(maker, sizes, *info):
    info["maker_name"] = maker
    info["sizes_num"] = sizes
    return info


info_msg = make_car("amercan", "china", "henan", "djfkl")
print(info_msg)
# 以上代码是根据书本上写出来的。
