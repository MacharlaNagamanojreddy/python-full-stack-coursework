#Ecommerce website
# that can add view and delete products from the inventory. Each product has a name, price, and quantity.
#I dont need example usage, just the code for the classes and methods.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def delete_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]
def main():
    inventory = Inventory()
if __name__ == "__main__":
    main()