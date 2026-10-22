class Product:
    def __init__(self, name, price, stock):
        self.stock = stock
        self.name = name
        self.price = price
        def update_stock(self, amt):
            self.stock += amt
        print(f"There are {self.stock} {self.name} items now")
        def info(self):
            return f"{self.name} - ${self.price} : {self.stock}"

