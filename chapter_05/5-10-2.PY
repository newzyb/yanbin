current_users = ["zhuyanbin", "limingxin", "hailong", "yangwei", "zhangchao"]
new_users = ["ZHUYANBIN", "hetingcan", "LIMINGXIN", "zhangchao", "XIjiande"]

new_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print(f"{new_user} in.")
    else:
        print(f"{new_user} out.")
