import json
import pathlib

number_file = pathlib.Path("fav_number.json")

if number_file.exists():
    content = number_file.read_text()
    if len(content) > 0:  # Checks if its empty.
        try:
            int(content)
        except ValueError:
            raise ValueError("VALUE STORED IS NOT A NUMBER!")
        load = json.loads(content)
        print(f"Your favorite number is {load}!")
    else:
        print("It seems you dont have a favorite number... ☹️ (NO DATA IN FILE)")
else:
    print("It seems you dont have a favorite number... ☹️ (FILE NOT FOUND)")
