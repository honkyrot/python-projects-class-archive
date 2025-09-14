import json
import pathlib

number_file = pathlib.Path("fav_number.json")

fav_number = input("What is your favorite number?\n>")
try:
    fav_number = int(fav_number)
except ValueError:
    print("NOT A NUMBER!!!")
else:
    print(f"Thank you for your favorite number! ({fav_number}) 😊")
    content = json.dumps(fav_number)
    number_file.write_text(content)
