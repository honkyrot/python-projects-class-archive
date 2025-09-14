import random


class Die:
    def __init__(self, max_sides):
        self.max_sides = max_sides
        self.current_side = 1

    def roll(self, amt=1):
        for gacha in range(amt):
            rng = random.randint(1, self.max_sides)
            print(f"Die has rolled a {rng}")
            self.current_side = rng


new_die = Die(6)
new_die.roll(10)
