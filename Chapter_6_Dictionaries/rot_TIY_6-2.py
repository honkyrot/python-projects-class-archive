usernames = [
    {"userName": "Jerry3756", "favNumber": 20},
    {"userName": "GGMASTER987", "favNumber": 987},
    {"userName": "CheesyBIG MAC17", "favNumber": 17},
    {"userName": "Bat Venom2187", "favNumber": 2187},
    {"userName": "WaffleSlayer06", "favNumber": 6}
]

for data0 in usernames:
    for key1, data1 in data0.items():
        print(f"{key1} = {data1}")
    print()

usernames.append({"userName": "Meggabad", "favNumber": 15})
usernames.append({"userName": "LukeCage06", "favNumber": 16})

print("New users added!\n")

for data0 in usernames:
    for key1, data1 in data0.items():
        print(f"{key1} = {data1}")
    print()
