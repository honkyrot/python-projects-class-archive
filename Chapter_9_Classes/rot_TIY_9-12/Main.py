from Users import User
from Admin import Admin, Privileges

user0 = User("Hong", "Rot", "Jerry3756")
user0.describe_user()
user0.greet_user()

user1 = Admin("Jayden", "Stout", "admin")
user1.describe_user()
print(Privileges.show_privileges(user1.privileges))
