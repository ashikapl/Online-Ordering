from controller.user import UserController
from controller.product import ProductController
from controller.cart import CartController
from controller.order import OrderController

#-------- Online Ordering (Mini Amazon) (Oops & Solid Based)--------#
def main():
    user = UserController()
    product = ProductController()
    cart = CartController()
    order = OrderController()

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
                admin_name = input("Enter the name:- ")
                admin_username = input("Enter the username:- ")
                user.add_user(admin_name, admin_username, "Admin")
                admin = user.get_user(admin_username)

                if admin_username == admin:
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
                                product.add_product(name, price)
                            case 2:
                                product.get_product()
                            case 3:
                                name = input("Enter the name of product you want to delete:- ")
                                product.remove_product(name)
                            case 4:
                                user.remove_user(admin_username)
                                break
                            case _:
                                print("Invalid Option!")
                else:
                    print("Admin Not Found!")

            case 2:
                name = input("Enter name:- ")
                username = input("Enter username:- ")
                user.add_user(name, username, "User")
                u = user.get_user(username)

                if username == u:
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
                                product.get_product()
                            case 2:
                                product_id = int(input("Enter the product_id you want add:- "))
                                quantity = int(input("Enter the quantity of product:- "))
                                cart.add_to_cart(product_id, quantity)
                            case 3:
                                cart.get_cart()
                            case 4:
                                item = input("Enter the cart id to place order:- ")
                                # total = order.total_amount(item)
                                payment_method = input("Enter the payment method:- ")
                                order.place_order(item, 0, payment_method)
                            case 5:
                                user.remove_user(username)
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
