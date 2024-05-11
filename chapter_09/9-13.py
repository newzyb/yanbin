from random import randint


class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides
        pass

    def roll_die(self):
        return randint(1, self.sides)


die6 = Die()

resluts = []
for ras in range(15):
    reslut = die6.roll_die()
    resluts.append(reslut)
print(resluts)
