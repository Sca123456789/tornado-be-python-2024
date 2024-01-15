
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def introduce(self):
#         print(f"Our restaurant name is {self.restaurant_name}. and we serve {self.cuisine_type}")

# class Admin(Restaurant):
#     privileges = ["can add new items to menu", "can view financial reports", "can hire new staff"]
    
#     def __init__(self, restaurant_name):
#         super().__init__(restaurant_name, "Admin")

#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(f"An admin can: {privilege}")

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


# Creating an instance of the Admin class
admin_user = Admin("admin_user")

# Showing username
admin_user.show_username()

# Showing privileges
admin_user.show_privileges()
