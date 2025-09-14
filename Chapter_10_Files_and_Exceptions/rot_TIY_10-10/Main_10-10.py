import pathlib

ebook_file = pathlib.Path("via_berlin_by_crittenden_mariott.txt")
content = ebook_file.read_text(encoding='utf-8')

total_character_count = len(content)
total_word_count = len(content.split())
word_count = content.lower().count("berlin")

print(f"There are a total of {total_character_count} characters in the story.")
print(f"There are a total of {total_word_count} words in the story.")
print(f"There are {word_count} words that are \"Berlin\"")
