class Cart:
    def __init__(self):
        self.item={}
        self.prices={'chocolate':5,'dark':10,'cool drink':20}

    def add_item(self,item_name,quantity):
        self.item[item_name]=quantity

    def get_items(self):
        cart_items=[]
        for item_name in self.item.items():
            cart_items.append(item_name)
        return cart_items
    
    def remove_items(self,item_name):
        del self.item[item_name]

    def update_items(self,item_name,updated_quantity):
        self.item[item_name]=updated_quantity

    def total_price_items(self):
        total_price=0
        for itm,quantity in self.item.items():
            total_price +=self.prices[itm]*quantity
        return total_price


    


obj=Cart()
obj.add_item('chocolate',5)
obj.add_item('dark',6)
obj.add_item('cool drink',10)
# obj.add_item('chocos',8)
# print(obj.get_items())
# (obj.remove_items('dark'))
# print(obj.get_items())
print(obj.item)
# obj.update_items('chocolate',50)
# print(obj.item)
print(obj.total_price_items())


