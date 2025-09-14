import pathlib

txt_file = pathlib.Path("learning_python.txt")
content = txt_file.read_text()
print(content)

lines = content.splitlines()

for line in lines:
    print(line)
