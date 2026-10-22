from product import Product

class physical_products(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock)
        self.weight = weight

    def Shipping(self):
        return 5.0 + (self.weight * 2.0)

    def info(self):
        base_info = super().info
        shipping = self.Shipping()
        return f"{base_info} | weifght : {self.weight}kg | Shipping fee : ${shipping:.2f}"

