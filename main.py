from digital_product import DigitalProduct
from physical_product import PhysicalProduct

laptop = PhysicalProduct("Lenovo LOQ", 980, 5, 2.5)
ebook = DigitalProduct("Harry Potter", 25, 100, 45)

products = [laptop, ebook]

print("<------Welcome to the store------>")
for item in products:
    print(item.info())
    if isinstance(item, DigitalProduct):
        print(f"   -> Link: {item.download_link()}")
    print("-" * 50)

print("\n[test purchase]")
laptop.update_stock(-1)
print(laptop.info())