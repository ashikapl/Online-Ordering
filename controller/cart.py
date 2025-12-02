from models.cart import Cart
from controller.product import ProductController 

class CartController:
        
    carts = []
    products = ProductController().products

        
    def add_to_cart(self, product_id, quantity):
        for i, val in enumerate(self.products, start=1):
            if product_id == i:
                cart = Cart(val.name, val.price, quantity)
                self.carts.append({val:cart})
            else:
                print("There is No Product_Id Found!")

    
    def get_cart(self):
        for i, cart_item in enumerate(self.carts, start=1):
            product = cart_item.products
            qty = cart_item.quantity

            print(f"{i}. {product.products_name}, ₹{product.product_price} - Qty: {qty}")

        