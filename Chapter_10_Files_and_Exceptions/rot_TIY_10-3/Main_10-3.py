import pathlib

txt_file = pathlib.Path("learning_python.txt")
content = txt_file.read_text()

print(content)

for line in content.splitlines():
    print(line)
