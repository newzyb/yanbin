class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


eric = User("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()
eric.greet_user()


eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(eric.login_attempts)
# 括号内为什么用eric,而不是写出来eric.变量名？
# 类里面列出来的所有属性都是实例的属性，可以直接用eric.属性名。
eric.reset_login_attempts()
print(eric.login_attempts)
