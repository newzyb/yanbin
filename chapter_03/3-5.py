guest_list = ["hetingcan", "limingxin", "zhangchao", "xijiande"]


name = guest_list[0].title()
print(f"Dear {name}, welcome to my dinner.")

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

print(guest_list)
