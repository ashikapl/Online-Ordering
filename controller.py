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
            user = User()
            self.users.append(user.set_user(username, name))
            print(self.users)
        else:
            print("User Already Exists!")


    def get_user(self, username):
        for user in self.users:
            if username in user:
                # print("Username:- ", user[username])
                return user[username]
            else:
                print("User Not Found!")


    def remove_user(self, username):
        for i, user in enumerate(self.users):
            if username in user:
                self.users.pop(i)
                # print(self.users)
            else:
                print("User Not Found!")
                

    # Products Operation
    def add_product(self, admin, name, price):
        if admin == self.admin:
            product = Product()
            self.products.append(product.add_product(name, price))
            print("Product Added Successfully!")
            print(self.products)
        else:
            print("Invalid Admin!")


    def get_product(self):
        for i, (name, price) in enumerate(self.products, start=1):
            print(f"{i}. {name} - ₹{price}")
    
    
    def remove_product(self, name):
        for i, p in enumerate(self.products):
            if p[0] == name:
                self.products.pop(i)
                print("Product Removed Successfully!")
                return
        print("Product Not Found!")
 
