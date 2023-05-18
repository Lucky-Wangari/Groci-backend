class Order:
    # Attributes
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount

    def get_order_id(self):
        return f"{self.order_id}" 
    def get_customer_name(self):
        return f"{self.customer_name}"
    def get_total_amount(self):
        return f"{self.total_amount}"
    def calculate_discounted_amount(self, discount_percentage):
        return f"{self.total_amount - (self.total_amount * discount_percentage / 100)}"

