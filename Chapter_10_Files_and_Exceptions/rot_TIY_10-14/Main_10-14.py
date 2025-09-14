import json
import pathlib


def get_stored_data(path):  # Get stored data
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None


def get_new_data(path):  # Write new data
    user_data_name = input("What is your name?\n>").title()
    user_data_hobby = input("What is your hobby?\n>")
    user_data_like = input("What is something you like?\n>")
    final_user_data = {"name": user_data_name, "hobby": user_data_hobby, "like": user_data_like}  # dictionary
    contents = json.dumps(final_user_data)
    path.write_text(contents)
    return final_user_data


def greet_user():  # User stuff
    path = pathlib.Path('username.json')
    user_data = get_stored_data(path)
    if user_data:  # Check if user exists
        print(f"Welcome back, {user_data['name']}!")
        confirm_data = input("Is this you? (y/n)\n>").lower()
        if confirm_data == "y" or confirm_data == "yes":  # Confirm if this is the correct user.
            print(f"Your hobbies are {user_data['hobby']}.")
            print(f"You like {user_data['like']}!")
            delete_test = input("(delete value? (y/n))\n>").lower()
            if delete_test == "y" or delete_test == "yes":
                path.unlink()
        else:  # If invalid user, overwrite the values.
            new_user_data = get_new_data(path)
            print(f"We'll remember you when you come back, {new_user_data['name']}!")
    else:  # Store new user if user does not exist.
        new_user_data = get_new_data(path)
        print(f"We'll remember you when you come back, {new_user_data['name']}!")


greet_user()  # Start
