print("Welcome to addition!")

first_value = input("Enter the first number\n>")
try:
    first_value = int(first_value)
except ValueError:
    raise ValueError("Please input a number!")
second_value = input("Enter the second number\n>")
try:
    second_value = int(second_value)
except ValueError:
    raise ValueError("Please input a number!")
print(f"{first_value} + {second_value} = {first_value+second_value}")
