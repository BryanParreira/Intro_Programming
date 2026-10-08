def items_purchase(store, wallet):
    can_buy = []
    for item, price in store.items():
        if price <= wallet:
            can_buy.append(item)
    can_buy.sort()
    return can_buy


print(items_purchase({"Water": 1, "Bread": 3, "TV": 1000}, 300))
print(items_purchase({"Apple": 4, "Pan": 100, "Spoon": 2}, 100))
print(items_purchase({"Phone": 999, "Laptop": 5000, "PC": 1200}, 1))
