class User:
    # users = []

    def __init__(self, name, username, role):
        self.name = name
        self.username = username
        self.role = role


    def set_user(self, name, username, role):
        self.name = name
        self.username = username
        self.role = role
        return {username:{name,role}}


    # def get_user(self, username):
    #     if username in self.users:
    #         return self.users
    #     else:
    #         print("User Not Found!")
