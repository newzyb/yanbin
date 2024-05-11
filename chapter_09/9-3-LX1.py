class User:
    def __init__(self, first_name, last_name, full_name, email, location) -> None:
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = full_name.title()
        self.emali = email.title()
        self.location = location.title()

        pass

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Full name: {self.full_name}")
        print(f"Email: {self.emali}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.last_name}")


eric = User("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()
eric.greet_user()
