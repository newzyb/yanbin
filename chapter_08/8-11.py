def show_message(msgs):
    for msg in msgs:
        print(msg)


# 自己写的send_messages.pop()是一个错误写法，正确的是 current_messages = msgs.pop()
def send_messages(msgs, sent_messages):
    while msgs:
        current_messages = msgs.pop()
        print(current_messages)
        sent_messages.append(current_messages)


msgs = ["you name is:", "what are you doing?", "where are you from?"]
show_message(msgs)

# 在这里，首先定义了一个空列表
sent_messages = []
send_messages(msgs[:], sent_messages)


print("\nFinal lists:")
print(msgs)
print(sent_messages)
