import random

# v1.1
number_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]  # hex
winning_numbers = []
winning_chances = 4  # set the winning numbers, higher = better chance to win
win_length = 4  # set how long the matching number must be, higher = lower chance to win

for i in range(winning_chances):  # make X random winning Y sets of letters and numbers
    set_numbers = ""
    for _ in range(win_length):
        set_numbers += random.choice(number_choices)
    winning_numbers.append(set_numbers)

print(f"The winning numbers: " + ", ".join(winning_numbers))
attempts = 0
active = True

while active:
    attempts += 1
    my_ticket = ""
    for _ in range(win_length):
        my_ticket += random.choice(number_choices)
    print(f"{my_ticket}")
    for winning_set in winning_numbers:
        if my_ticket == winning_set:
            print(f"Winning number! {my_ticket} = {winning_set} in {winning_numbers} with {attempts} attempts!")
            active = False
            break
