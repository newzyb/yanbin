from user import Admin

eric = Admin("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()

eric_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
