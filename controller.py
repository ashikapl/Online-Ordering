from models.user import User
from models.product import Product

class Controller:
    users = []
    products = []
    admin = ""

    # Admin Operation
    def add_admin(self, admin):
        if self.admin == "":
            self.admin = admin
            print("Admin Added Successfully!")
        else:
            print("Admin Already Exists!")


    def remove_admin(self, admin):
        if admin == self.admin:
            self.admin = ""
            print("Admin Deleted Successfully!")
        else:
            print("Admin Not Found!")


    # Users Operation
    def add_user(self, name, username):
        if username not in self.users:
            user = User(name, username)
            self.users.append({username:user})
            print(self.users)
        else:
            print("User Already Exists!")


    def get_user(self, username):
        for user in self.users:
            if username in user:
                print("Username:- ", user[username])
                return user[username]
        print("User Not Found!")


    # User remove


    # Products Operation
    def add_product(self, admin, name, price):
        if admin == self.admin:
            product = Product(name, price)
            self.products.append(product)
            print(self.products)
        else:
            print("Invalid Admin!")

    # get
    # remove
 
