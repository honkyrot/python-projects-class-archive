import pathlib

path = pathlib.Path("guest_list.txt")

guest = input("Hello guest! What is your name?\n>").title()
path.write_text(guest)
print(f"Thank you {guest} for your time.")
