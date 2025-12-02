from models.user import User

class UserController:
    
    users = []


    def add_user(self, name, username, role):
        if username not in self.users:
            user = User(name, username, role)
            self.users.append(user)
            if role == "Admin":
                print("Admin Added Successfully!")
            else:
                print("User Added Successfully!")
            # print(self.users)
        else:
            print("User Already Exists!")


    def get_user(self, username):
        for user in self.users:
            if username == user.username:
                # print("Username:- ", user[username])
                return user.username
            else:
                print("User Not Found!")


    def remove_user(self, username):
        for i, user in enumerate(self.users):
            if username == user.username:
                self.users.pop(i)
                if user.role == "Admin":
                    print("Admin Deleted Successfully!")
                else:
                    print("User Deleted Successfully!") 
                # print(self.users)
            else:
                print("Not Found!")
                