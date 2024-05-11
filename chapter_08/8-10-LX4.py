def show_messages(msgs):
    for msg in msgs:
        print(msg)


def send_messages(msgs, sent_messages):
    while msgs:
        current_messages = msgs.pop()
        print(current_messages)
        sent_messages.append(current_messages)
        # print(sent_messages)


# 多写了一个Print,把sent_messages列表给打印出来了。

msgs = ["you name is:", "what are you doing?", "where are you from?"]
show_messages(msgs)

print("-----------------------------")
sent_messages = []
send_messages(msgs, sent_messages)

print("-----------------------------")
print(msgs)
print(sent_messages)
