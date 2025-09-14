from Users import User


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        return f"administrative privileges: {self.privileges}"


class Admin(User):
    def __init__(self, fn, ln, un):
        super(Admin, self).__init__(fn, ln, un)
        self.privileges = Privileges(["can ban users", "can delete posts", "can announce posts", "can add posts"])
