def show_messages(msgs):
    for msg in msgs:
        print(msg)


msgs = ["you name is:", "what are you doing?", "where are you from?"]
show_messages(msgs)


def send_messages(msgs, sent_messages):
    while msgs:
        current_messages = msgs.pop()
        print(current_messages)
        sent_messages.append(current_messages)
        print(sent_messages)


send_message = []
send_messages(msgs, sent_messages)
# 在这里，错误定义了变量send_message，导致后面调用函数(sent_messages)一直报错。

print("---")
