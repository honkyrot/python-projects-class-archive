pet_0 = {"type": "cat", "owner": "Hong"}
pet_1 = {"type": "dog", "owner": "Bill"}
pet_2 = {"type": "dog", "owner": "Oswald"}
pet_3 = {"type": "ferret", "owner": "Gerald"}
pet_4 = {"type": "cat", "owner": "Jill"}

all_pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in all_pets:
    print(f"The pet {pet['type']} is currently owned by {pet['owner']}.")
