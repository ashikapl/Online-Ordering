from models.cart import Cart
from controller.product import ProductController 

class CartController:
        
    carts = []
    products = ProductController().products

        
    def add_to_cart(self, product_id, quantity):
        if 1 <= product_id <= len(self.products):
            val = self.products[product_id-1]
            cart = Cart(val.name, val.price, quantity)
            self.carts.append(cart)
            print("Added to Cart!")
        else:
            print("There is No Product_Id Found!")

    
    def get_cart(self):
        for i, cart_item in enumerate(self.carts, start=1):
            print(f"{i}. {cart_item.product_name} - ₹{cart_item.product_price} -> Quantity:- {cart_item.quantity}")

        