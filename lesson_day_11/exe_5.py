import os
import os

class User:
    
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"User Profile: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("John", "Doe", 0)
user2 = User("Alice", "Smith", 0)


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


def increment_login_attempts(user):
    file_path = "login_attempts.txt"

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the current count from the file
        with open(file_path, 'r') as file:
            attempts_count = int(file.read())
    else:
        # If the file doesn't exist, initialize the count to 0
        attempts_count = 0

    # Increment the attempts count
    attempts_count += 1

    # Update the file with the new count
    with open(file_path, 'w') as file:
        file.write(str(attempts_count))

    # Update the user's login attempts count
    user.login_attempts = attempts_count

    return attempts_count

# Call the function to get and update the attempts count
attempts = increment_login_attempts(user1)

print(f"number of attemts: {attempts}")
