from models.product import Product

class ProductController:
    
    products = []
    

    def add_product(self, name, price):
        # if admin == self.admin:
            product = Product(name, price)
            self.products.append(product)
            print("Product Added Successfully!")
            print(self.products)
        # else:
        #     print("Invalid Admin!")


    def get_product(self):
        for i, p in enumerate(self.products, start=1):
            print(f"{i}. {p.name} - ₹{p.price}")
    
    
    def remove_product(self, name):
        # if admin == self.admin:
            for i, p in enumerate(self.products):
                if p.name == name:
                    self.products.pop(i)
                    print("Product Removed Successfully!")
                    return
            print("Product Not Found!")
        # print("Admin Not Found!")
