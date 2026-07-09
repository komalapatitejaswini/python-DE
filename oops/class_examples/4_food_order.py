class FoodOrder:

    restaurant = "Domino's"

    def __init__(self, customer_name, food_item):
        self.customer_name = customer_name
        self.food_item = food_item

    def place_order(self):
        return f"{self.food_item} ordered"

    @classmethod
    def restaurant_name(cls):
        return cls.restaurant

    @staticmethod
    def delivery_time():
        return "Delivery in 30 minutes"

    @property
    def order_status(self):
        return "Order Confirmed"

    def order_details(self):
        return (
            f"Customer      : {self.customer_name}\n"
            f"Food placed   : {self.place_order()}\n"
            f"Restaurant    : {self.restaurant_name()}\n"
            f"Delivery time : {self.delivery_time()}\n"
            f"Status        : {self.order_status}"
        )

order1 = FoodOrder("Teja", "Non-veg Pizza")

print(order1.customer_name)
print(order1.food_item)
print(order1.order_details())

