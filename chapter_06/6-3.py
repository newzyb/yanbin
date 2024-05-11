glossary = {
    "str": "Strings implement all of the common sequence operations.",
    "list": "The constructor builds a list whose items are the same and in the same order as iterable’s items.",
    "tuple": "it is actually the comma which makes a tuple, not the parentheses.",
    "range": "If the step argument is omitted, it defaults to.",
    "set": "The elements of a set must be hashable.",
}

s = glossary["str"].title()
print(f"str: {s}")

l = glossary["list"]
print(f"\nlist: {l}")

t = glossary["tuple"].title()
print(f"\ntuple: {t}")

r = glossary["range"]
print(f"\nrange: {r}")

se = glossary["set"]
print(f"\nset: {se}")
