print("Welcome to addition!")
print("Type 'quit' to quit.")

while True:
    first_value = input("Enter the first number\n>").lower()
    if first_value == "quit":
        break
    try:
        first_value = int(first_value)
    except ValueError:
        print("Please input a number!")
        continue
    second_value = input("Enter the second number\n>").lower()
    if second_value == "quit":
        break
    try:
        second_value = int(second_value)
    except ValueError:
        print("Please input a number!")
        continue
    print(f"{first_value} + {second_value} = {first_value+second_value}")
