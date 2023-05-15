class Order:
    def __init__(self,name,items_ordered,total_price):
        self.name =  name
        self.items_ordered = items_ordered
        self.total_price = total_price
  
    def calculate_order_total(self, item, total_price):
        sum = 0
        for item in total_price:
            sum += item
            print(sum)
           
            order = Order()
            order.calculate_order_total(name= "Omyra", item_ordered= "Kales", total_price= 50)
            order.calculate_order_total(name = "Rarmani",item_ordered= "Potatoes", total_price= 170 )
        print(f"This is your total {self.calculate_order_total}")
           
       
    def list_of_items(self,item, items_ordered):
        result = []
        for item in items_ordered:
            if item == items_ordered:
                result.append(item)
           
            print(result)
        
           
