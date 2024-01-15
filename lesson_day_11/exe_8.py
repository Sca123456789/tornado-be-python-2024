class User:
    def __init__(self, username):
        self.username = username

    def show_username(self):
        print(f"Username: {self.username}")


class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Privileges for {self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")



admin_user = Admin("admin_user")

admin_user.show_username()

admin_user.show_privileges()


