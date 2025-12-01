class User:
    # users = []

    def __init__(self, name="", username=""):
        self.name = name
        self.username = username


    def set_user(self, name, username):
        self.name = name
        self.username = username
        return {username:name}


    def get_user(self, username):
        if username in self.users:
            return self.users
        else:
            print("User Not Found!")
