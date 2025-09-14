import pathlib

txt_file = pathlib.Path("learning_python.txt")
content = txt_file.read_text()
content = content.replace("Python", "Lua")  # Python to Lua

print(content)

content = content.replace("Lua", "C")  # Lua to C

lines = content.splitlines()

for line in lines:
    print(line)
