send_messages = ["you name is:", "what are you doing?", "where are you from?"]
sent_messages = []
while send_messages:
    current_messages = send_messages.pop()
    print(current_messages)

    sent_messages = current_messages.append()

print("---")
for sent_message in sent_messages:
    print(sent_message)

# sent_messages = current_messages.append()这种写法是错误的。
# append()方法正确的用法是，把要添加的元素写到它后面的括号内。如：append('')
