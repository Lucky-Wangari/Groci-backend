
class Product:
   def __init__(self, name, price, description,):
       self.name = name
       self.price = price
       self.description = description
       self.cart = []
      
   def confirm_availability(self):
       for i in self.name:
           if i in self.cart.append(self.name):
             print(f"{self.description} {self.name} are available at {self.price}")
       else:
           print(f"{self.description} {self.name} are not available")
          
   def calculate_order_total(self, item):
       sum = 0
       for item in self.price:
           sum += item
       print(sum)
      
   def change_order(self, item):
       if item in self.name:
        self.cart.replace(self.name)
        print(f"New order {self.name} {self.price}")