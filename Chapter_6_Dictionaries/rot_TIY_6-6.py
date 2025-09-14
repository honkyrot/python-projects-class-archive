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
        print(f"Hello, we would like you to take our poll.")
