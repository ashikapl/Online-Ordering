from models.order import Order

class OrderController:
     
    orders = []

    def place_order(self, items, amount, payment_method):
        print(items)
        order = Order(items, amount, payment_method)
        self.orders.append(order)
        order.order_id += 1