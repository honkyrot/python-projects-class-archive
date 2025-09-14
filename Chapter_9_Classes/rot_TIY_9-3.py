class User:
    def describe_user(self):
        print(f"Username: {self.username}, Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.username}! How are you doing?")

    def __init__(self, fn, ln, un):
        self.first_name = fn
        self.last_name = ln
        self.username = un


user1 = User("Hong", "Rot", "Jerry3756")
user1.describe_user()
user1.greet_user()

user2 = User("Jayden", "Stout", "GGMASTER987") # just using friend names
user2.describe_user()
user2.greet_user()

user3 = User("Cody", "Krick", "Bat Venom2187")
user3.describe_user()
user3.greet_user()
