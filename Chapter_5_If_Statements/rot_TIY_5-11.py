numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numberList:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif 3 < number < 21:
        print(f"{number}th")
