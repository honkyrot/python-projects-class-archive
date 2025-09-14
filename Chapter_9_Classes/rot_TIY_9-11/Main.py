from Users import *

user1 = Admin("Jayden", "Stout", "admin")
user1.describe_user()
print(Privileges.show_privileges(user1.privileges))
