import json
import pathlib

number_file = pathlib.Path("fav_number.json")


def write_to_file():
    fav_number = input("What is your favorite number?\n>")
    try:
        fav_number = int(fav_number)
    except ValueError:
        print("NOT A NUMBER!!!")
    else:
        print(f"Thank you for your favorite number! ({fav_number}) 😊")
        write_content = json.dumps(fav_number)
        number_file.write_text(write_content)


if number_file.exists():
    content = number_file.read_text()
    if len(content) > 0:  # Checks if its empty.
        try:
            int(content)
        except ValueError:
            raise ValueError("DATA STORED IS NOT A NUMBER!")
        load = json.loads(content)
        print(f"Your favorite number is {load}!")
        delete_test = input("delete value? (y/n)\n>").lower()
        if delete_test == "y" or delete_test == "yes":
            number_file.unlink()
    else:
        print("It seems you dont have a favorite number... ☹️ (NO DATA IN FILE)")
        write_to_file()
else:
    write_to_file()
