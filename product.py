class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        self.stock += amount

    def info(self):
        return f"{self.name} - ${self.price:.2f} : {self.stock} in stock"
