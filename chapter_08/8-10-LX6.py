def show_messages(messages):
    for msg in messages:
        print(msg)


# current_msg = send_messages.pop()定义错了参数，正确的应该是current_msg = messges.pop()
# sent_messages.append(current_msg)下面也没有print(sent_messages)语句，应该是最后调用的时候，写出来。
def send_messages(messges, sent_messages):
    while messges:
        current_msg = messges.pop()
        sent_messages.append(current_msg)


msgs = ["hello there", "how are u?", ":)"]
show_messages(msgs)

sent_messages = []
show_messages(sent_messages)

print("\nFinal lists:")
print(msgs)
print(sent_messages)
