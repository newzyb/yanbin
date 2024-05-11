def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        current_msgs = messages.pop()
        sent_messages.append(current_msgs)
    return sent_messages


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
