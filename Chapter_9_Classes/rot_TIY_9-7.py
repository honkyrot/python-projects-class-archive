import random


class User:
    def __init__(self, fn, ln, un):
        self.first_name = fn
        self.last_name = ln
        self.username = un
        self.login_attempts = 0

    def describe_user(self):
        print(f"Username: {self.username}, Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.username}! How are you doing?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def clear_logins(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, fn, ln, un):
        super(Admin, self).__init__(fn, ln, un)
        self.privileges = ["can ban users", "can delete posts", "can announce posts", "can add posts"]

    def show_privileges(self):
        return f"administrative privileges: {self.privileges}"


user1 = User("Hong", "Rot", "Jerry3756")
for i in range(random.randint(1, 20)):
    user1.increment_login_attempts()
    print(user1.login_attempts)
user1.clear_logins()
user1.describe_user()
user1.greet_user()
print(user1.login_attempts)  # Resets to 0!
print()  # break
user2 = Admin("Jayden", "Stout", "admin")
user2.describe_user()
print(user2.show_privileges())
