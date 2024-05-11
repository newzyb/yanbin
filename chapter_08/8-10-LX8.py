def show_messages(msgs):
    for msg in msgs:
        print(msg)


def send_messages(msgs, sent_messages):
    while msgs:
        current_msgs = msgs.pop()
        sent_messages.append(current_msgs)


msgs = ["you name is:", "what are you doing?", "where are you from?"]
show_messages(msgs)

sent_messages = []
send_messages(msgs, sent_messages)

print(msgs)
print(sent_messages)
