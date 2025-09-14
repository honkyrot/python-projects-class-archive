people = {
    "person0": {"first_name": "Hong", "last_name": "Rot", "age": 16, "city": "Fort Wayne"},
    "person1": {"first_name": "Cody", "last_name": "Krick", "age": 16, "city": "Fort Wayne"},
    "person2": {"first_name": "Brady", "last_name": "Zuber", "age": 17, "city": "Fort Wayne"},
    "person3": {"first_name": "Lua", "last_name": "Son", "age": 14, "city": "Fort Wayne"},
    "person4": {"first_name": "Jayden", "last_name": "Stout", "age": 16, "city": "Fort Wayne"},
    "person5": {"first_name": "Nathan", "last_name": "Marshall", "age": 16, "city": "Fort Wayne"}
}

for key0, data0 in people.items():
    for key1, data1 in data0.items():
        print(f"{key1} = {data1}")
    print()
