class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def show_description(self):
        print(f"{self.name}: ${self.price}")

    def __str__(self):
        return f"{self.name} (${self.price})"


class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)

    def display_menu(self):
        for item in self.menu_items:
            item.show_description()

    def lunch_menu(self):
        # $2 cheaper; do NOT change the real prices
        for item in self.menu_items:
            print(f"{item.name}: ${item.get_price() - 2}")

    def __str__(self):
        return f"{self.restaurant_name} ({len(self.menu_items)} items)"


restaurant = Restaurant("Joe's Diner")
restaurant.add_menu_item(MenuItem("Burger", 10))
restaurant.add_menu_item(MenuItem("Salad", 8))
print(restaurant)
restaurant.display_menu()
restaurant.lunch_menu()
