send_messages = ["you name is:", "what are you doing?", "where are you from?"]
sent_messages = []
while send_messages:
    current_messages = send_messages.pop()
    print(current_messages)

    sent_messages.append(current_messages)

print("---")
for sent_message in sent_messages:
    print(sent_message)
