toppings = ["mushrooms", "green peppers", "extra cheese"]
for topping in toppings:
    print(f"Adding {topping}.")
print("\nfinished making you pizza!")
# 240403--明白了，不理解书中这条代码的意思：为什么添加了topping，就可以遍历列表呢？
# 原来，topping还是一个变量，并没有明确的指出它是哪一个确定的值。
# 而IN和等于号是一样的，也就是把列表赋值给了topping，把列表里的值给全部打印了出来。
