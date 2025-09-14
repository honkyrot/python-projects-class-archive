favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

new_people = [
    "hong",
    "cody",
    "phil",
    "jayden",
    "nathan",
    "jen",
]

for data0 in new_people:
    if data0 in favorite_languages:
        print(f"Thank you for responding to the poll, {data0.title()}.")
    else:
        print(f"Hello, {data0.title()}, we would like you to take our poll.")  # PROGRAM WILL TAKE THE POLL.
        newlang = input("Please type your favorite language.\n")
        favorite_languages.update({data0.lower(): newlang.lower()})  # PROGRAM WILL INSERT NEW LANGUAGE

print(favorite_languages)
