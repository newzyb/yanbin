class User:
    def __init__(
        self,
        first_name,
        last_name,
        username,
        email,
        location,
    ):
        self.name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.name} {self.last_name} is messages.")
        print(f"username: {self.username}")
        print(f"email: {self.email}")
        print(f"location: {self.location}")

    def greet_user(self):
        msg = f"Hello, {self.last_name}."
        print(msg)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


full_name = User("willie", "burger", "willieburger", "wb@example.com", "alaska")
full_name.describe_user()
full_name.greet_user()


eric = User("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()
eric.greet_user()

eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"{eric.login_attempts}")

eric.reset_login_attempts()
print(f"{eric.login_attempts}")
