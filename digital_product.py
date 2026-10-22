from product import Product
from physical_product import info 

class Digital_produc(Product):
    def __init__(self, name, price, stock, file_size):
        super().__init__(name, price, stock)
        self.file_size = file_size
    def download_link(self):
        name = self.name.lower().replace("", "-")
        return f"https://local_store.com/dowmload/{name}"
    def info(self):
        base_info = super.get(info)
        return f"{base_info} | size : {self.file_size}Mb"