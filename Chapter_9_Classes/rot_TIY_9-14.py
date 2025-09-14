import random

number_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]  # hex
winning_numbers = []

for i in range(4):  # make 4 random winning numbers and make a 4 combo match
    set_numbers = ""
    for _ in range(4):
        set_numbers += random.choice(number_choices)
    winning_numbers.append(set_numbers)

print("Any set of numbers here are winning!")
for i in winning_numbers:
    print(i)
