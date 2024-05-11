def show_messages(msgs):
    for msg in msgs:
        print(msg)


def send_messages(msgs, sent_messages):
    while msgs:
        current_msgs = msgs.pop()
        sent_messages.append(current_msgs)


# current_msgs = msgs.pop()刚开始还是定义错了，写成了current_msgs = send_messages.pop().
# 还是没有完全理解意思，send_messages虽然是定义过了，但是，只是一个变量，没有真正的值。


# 在这里定义的变量名questions并不是上面的形参(msgs)，导致下面不能被执行。
# 被调用函数变量名不能乱定义，上面已经定义了for循环，下面调用的时候，要给形参msgs赋值。
questions = ["you name is:", "what are you doing?", "where are you from?"]
show_messages(questions)

sent_messages = []
send_messages(msgs, sent_messages)

print(msgs)
print(sent_messages)
