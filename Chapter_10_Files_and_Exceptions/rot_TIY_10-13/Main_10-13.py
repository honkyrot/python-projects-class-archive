import json
import pathlib


def get_stored_data(path):  # Read data
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None


def get_new_data(path):  # Store new data
    user_data_name = input("What is your name?\n>").title()
    user_data_hobby = input("What is your hobby?\n>")
    user_data_like = input("What is something you like?\n>")
    final_user_data = {"name": user_data_name, "hobby": user_data_hobby, "like": user_data_like}
    contents = json.dumps(final_user_data)
    path.write_text(contents)
    return final_user_data


def greet_user():  # Greet user
    path = pathlib.Path('username.json')
    user_data = get_stored_data(path)
    if user_data:  # If data exists, display data
        print(f"Welcome back, {user_data['name']}!")
        print(f"Your hobbies are {user_data['hobby']}!")
        print(f"You like {user_data['like']}!")
        delete_test = input("(delete value? (y/n))\n>").lower()
        if delete_test == "y" or delete_test == "yes":  # Delete data for next user
            path.unlink()
    else:  # If data does not exist, get user to store new data!
        username = get_new_data(path)
        print(f"We'll remember you when you come back, {username['name']}! ＞︿＜")


greet_user()
