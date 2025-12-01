class Product:
    # products=[]

    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    
    def add_product(self, name, price):
        # self.products.append((name, price))
        self.name = name
        self.price = price
        return (self.name, self.price)
 
 
    def get_products(self):
        print("----- Products -----")
        for i, (name, price) in enumerate(self.products, start=1):
            print(f"{i}. {name} - ₹{price}")

