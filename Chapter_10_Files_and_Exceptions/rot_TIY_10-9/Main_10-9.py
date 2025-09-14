import pathlib
# Move any of these files out to make them readable, else put it in the hidden_directory
# Now silent errors!
cat_file = pathlib.Path("cats.txt")
dog_file = pathlib.Path("dogs.txt")

try:
    content = cat_file.read_text()
    print(content)
except FileNotFoundError:
    pass
    # print(f"File {cat_file} not found!")

try:
    content = dog_file.read_text()
    print(content)
except FileNotFoundError:
    pass
    # print(f"File {dog_file} not found!")
