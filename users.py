class Users:
    def __init__(self, email, name, password, title):
        self.email = email
        self.name = name
        self.password = password
        self.title = title

    def change_password(self, new_password):
        self.password = new_password

    def change_title(self, new_title):
        self.title = new_title

    def get_infor(self):
        print(f"User {self.name} works as {self.title}")


