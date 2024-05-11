class User:
    def __init__(self, first_name, last_name, username, email, location) -> None:
        self.name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        pass

    def describe_user(self):
        print(f"{self.name} {self.last_name} is messages.")
        print(f"username: {self.username}")
        print(f"email: {self.email}")
        print(f"location: {self.location}\n")

    def greet_user(self):
        msg = f"Hello, {self.last_name}.\n"
        print(msg)


full_name = User("willie", "burger", "willieburger", "wb@example.com", "alaska")
full_name.describe_user()
full_name.greet_user()


eric = User("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()
eric.greet_user()
