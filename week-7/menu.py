# (a)
menu = {}
menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3

# (b)
for item, price in menu.items():
    print(item, "cost", price)
