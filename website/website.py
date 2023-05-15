class Website:
   def __init__(self, product, order):
       self.product = product
       self.order = order
      
   def add_product(self,item):
        print(f"{self.product}")
      
   def special_offers(self):
       print(f"{self.order} fruits and get a lire of milk free")
      
   def decribe_product(self):
       print(f"{self.product} are available for purchase, both online and in store")
  
   def check_out(self):
       print(f"{self.order} confirmed")

