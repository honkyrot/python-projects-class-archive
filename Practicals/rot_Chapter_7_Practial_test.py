og_restaurants = ["burger king", "dairy queen", "chick fil a", "kfc", "subway"]
user_database = {}
max_users = 8   # set maximum users to answer the poll.
current_users = 0
# chapter 7 (v1.0) ⭐
while current_users < max_users:
    current_users += 1
    user_restaurant = []
    user_name = input("What is your name? : ").title()
    if user_name in user_database:  # does not take the same student.
        print("Sorry, it seems you have already taken this.")
        continue
    while True:
        user_input = input("Type what fast-food restaurant you like, when you are done type 'done'\n")
        if user_input.lower() == "done":
            break
        else:
            user_restaurant.append(user_input.title())
    print(f"Thank you for adding your restaurant, onto the next person. ({current_users}/{max_users})")
    user_data = {user_name: user_restaurant}
    user_database.update(user_data)
    for restaurant in user_restaurant:
        if restaurant.lower() not in og_restaurants:  # checks for duplicates, case-insensitive, spelling matters.
            og_restaurants.append(restaurant.lower())
            print(f"added new restaurant {restaurant}")
print(user_database)
