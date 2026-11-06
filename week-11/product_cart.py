class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def display_details(self):
        print(f"{self.name}: ${self.price}")

    def __str__(self):
        return f"{self.name} (${self.price})"


class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def __str__(self):
        return f"Cart {self.customer_id} ({len(self.products)} products)"


cart = ShoppingCart(101)
cart.add_product(Product("Pen", 2))
cart.add_product(Product("Notebook", 5))
print(cart)
print(cart.calculate_total())  # 7
