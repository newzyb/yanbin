from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winning_ticker = []
print("Let's see what the winning ticket is...")


while len(winning_ticker) < 4:
    pull_item = choice(possibilities)

    if pull_item not in winning_ticker:
        print(f"  We pulled a {pull_item}!")
        winning_ticker.append(pull_item)

print(f"We final winning ticker is {winning_ticker}")
