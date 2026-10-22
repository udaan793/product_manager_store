from product import Product


class DigitalProduct(Product):
    def __init__(self, name, price, stock, file_size):
        super().__init__(name, price, stock)
        self.file_size = file_size

    def download_link(self):
        name = self.name.lower().replace(" ", "-")
        return f"https://local_store.com/download/{name}"

    def info(self):
        return f"{super().info()} | size: {self.file_size}MB"