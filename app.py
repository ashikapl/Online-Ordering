from models.user import User
from models.product import Product
from controller import Controller

#-------- Online Ordering (Mini Amazon) (Oops & Solid Based)--------#
def main():
    controller = Controller()
    p = Product()

    while True:
        print()
        print("----Welcome To Mini Amazon----")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        print()
        choice = int(input("Enter the Choice:- "))
        print()

        match choice:
            case 1:
                admin = input("Enter the name:- ")
                controller.add_admin(admin)

                if admin == controller.admin:
                    while True:
                        print()
                        print("1. Add Product")
                        print("2. View Product")
                        print("3. Remove Product")
                        print("4. Logout")
                        print()
                        option = int(input("Enter the Option:- "))
                        print()
                        
                        match option:
                            case 1:
                                name = input("Enter the product name:- ")
                                price = float(input("Enter the price:- "))
                                controller.add_product(admin, name, price)
                            case 2:
                                controller.get_products()
                            case 3:
                                name = input("Enter the name of product you want to delete:- ")
                                controller.remove_product(name)
                            case 4:
                                controller.remove_admin(admin)
                                break
                            case _:
                                print("Invalid Option!")
                else:
                    print("Admin Not Found!")

            case 2:
                name = input("Enter name:- ")
                username = input("Enter username:- ")
                controller.add_user(name, username)

                if username in controller.users:
                    while True:
                        print()
                        print("1. View Products")
                        print("2. Add To Cart")
                        print("3. View Cart")
                        print("4. View Orders")
                        print("5. Logout")
                        print()
                        option = int(input("Enter the Option:- "))
                        print()

                        match option:
                            case 1:
                                controller.get_products()
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                controller.remove_user(username)
                                break
                            case _:
                                print("Invalid Option!")
                else:
                    print("User Not Found!")
            case 3:
                break
            case _:
                print("Invalid Choice!")


if __name__  == "__main__":
    main()
