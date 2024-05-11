current_users = ["zhuyanbin", "limingxin", "hailong", "yangwei"]
new_users = ["ZHUYANBIN", "hetingcan", "LIMINGXIN", "zhangchao"]

new_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print(f"{new_user}, you name in list.")
    else:
        print(f"{new_user}, you name not in list.")
