guest_list = ["hetingcan", "limingxin", "zhangchao", "xijiande"]
print(len(guest_list))

name = guest_list[0].title()
print(f"\nDear {name}, welcome to my dinner.")

name = guest_list[1].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[2].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[3].title()
print(f"sorry, {name} can't make it to dinner.")

del guest_list[3]
guest_list.insert(3, "hailong")

name = guest_list[0].title()
print(f"\nDear {name}, welcome to my dinner.")

name = guest_list[1].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[2].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[3].title()
print(f"Dear {name}, welcome to my dinner.")

print(f"{guest_list} I have got a big desk, please to my dinner.")

guest_list.insert(0, "zhangyanbin")
guest_list.insert(3, "luoshicong")
guest_list.append("zhangerwei")

name = guest_list[0].title()
print(f"\nDear {name}, welcome to my dinner.")

name = guest_list[1].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[2].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[3].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[4].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[5].title()
print(f"Dear {name}, welcome to my dinner.")

name = guest_list[6].title()
print(f"Dear {name}, welcome to my dinner.")

print(len(guest_list))
print(f"{guest_list} I am sorry to message you, only two guest to my dinner.")

name = guest_list.pop(0)
print(f"\n{name}, I am sorry to message you, you can't to my dinner.")

name = guest_list.pop()
print(f"{name}, I am sorry to message you, you can't to my dinner.")

name = guest_list.pop()
print(f"{name}, I am sorry to message you, you can't to my dinner.")

name = guest_list.pop()
print(f"{name}, I am sorry to message you, you can't to my dinner.")

name = guest_list.pop()
print(f"{name}, I am sorry to message you, you can't to my dinner.")
print(f"{guest_list} welcom to my dinner.")

del guest_list[0]
del guest_list[0]
print(guest_list)
