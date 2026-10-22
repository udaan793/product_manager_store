from product import Product


class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock)
        self.weight = weight

    def shipping(self):
        return 5.0 + (self.weight * 2.0)

    def info(self):
        base_info = super().info()
        return (
            f"{base_info} | weight: {self.weight}kg "
            f"| shipping fee: ${self.shipping():.2f}"
        )
