prices = {"flour": 2.50, "sugar": 1.80, "eggs": 3.00, "milk": 2.00,
          "butter": 2.75, "vanilla": 4.50, "chocolate": 5.00}


def total_cost(ingredients):
    total = 0
    for ingredient in ingredients:
        if ingredient in prices:
            total += prices[ingredient]
    return round(total, 2)


print(total_cost(["flour", "sugar", "eggs", "butter"]))
print(total_cost(["milk", "vanilla", "chocolate"]))
print(total_cost(["eggs", "eggs", "flour", "sugar"]))
