numberList = []
for number in range(1,11):  # list from 1-10
    numberList.append(number)
print(f"the first three numbers are {numberList[:3]}")
print(f"the middle four numbers are {numberList[3:7]}")
print(f"the last three numbers are {numberList[-3:]}")
