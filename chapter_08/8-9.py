def show_messages(msgs):
    for msg in msgs:
        print(msg)


msgs = ["you name is:", "what are you doing?", "where are you from?"]
show_messages(msgs)
# print(show_messages(msgs)) 使用了print多打印了一个空值-None，不需要print。
# 函数体内已经有print了，所以，最后只需要调用show_messages就可以了，最后写出来print是多余的。
# print(message)打印出来的是message里面的内容，函数循环体没有使用。
# print(show_messages(message))使用了函数循环，分别把三条信息给打印出来了。
