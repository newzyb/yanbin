current_users = ["zhuyanbin", "hetingcan", "limingxin", "zhangchao", "xijiande"]
new_users = ["zhuyanbin", "Zhangyanbin", "Hailong", "Chenxiaohu", "Hetingcan"]

new_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print(f"{new_user} can not use the name.")
    else:
        print(f"{new_user} can use the name.")
