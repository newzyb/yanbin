locals = ["hangzhou", "suzhou", "hainandao", "wuhan", "chongqing"]

print("\nOriginal order-1:")
print(locals)

print("\nAlphabetical:")
print(sorted(locals))

print("\nOriginal order-2:")
print(locals)

print("\nReverse alphabetical\b:")
print(sorted(locals, reverse=True))

print("\nOriginal order-3:")
print(locals)

locals.reverse()
print(f"\n{locals}")

locals.reverse()
print(f"\n{locals}")

locals.sort()
print(f"\n{locals}")

locals.sort(reverse=True)
print(f"\n{locals}")

print(len(locals))

locals.append(11)
print(locals)
