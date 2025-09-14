class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        return f"administrative privileges: {self.privileges}"


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
        self.privileges = Privileges(["can ban users", "can delete posts", "can announce posts", "can add posts"])
