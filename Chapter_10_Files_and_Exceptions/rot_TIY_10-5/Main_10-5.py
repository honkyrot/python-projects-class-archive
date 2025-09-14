import pathlib

path = pathlib.Path("guest_list.txt")

final_str = ""
while True:
    guest = input("Hello guest! What is your name? 'Quit' to quit.\n>").title()
    if guest == "Quit" or guest == "Q":
        break
    print(f"Thank you {guest} for your time.")
    final_str += f"{guest}\n"
path.write_text(final_str)
print(path.read_text())
