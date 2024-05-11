locals = ["hangzhou", "suzhou", "hainandao", "wuhan", "chongqing"]

print(len(locals))

locals.append("11")
print(locals)

locals.insert(2, "zhuyanbin")
print(locals)

poped_locals = locals.pop()
print(poped_locals)
print(locals)

pop_locals = locals.pop(4)
print(pop_locals)
print(locals)

locals.remove("hainandao")
print(locals)

locals.sort()
print(locals)

locals.sort(reverse=True)
print(locals)

print(sorted(locals))

locals.reverse()
print(locals)
