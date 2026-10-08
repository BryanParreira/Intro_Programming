def total_sales(sales):
    total = 0
    for product in sales:
        total += sales[product]
    return total


print(total_sales({"Laptop": 5, "Phone": 10, "Tablet": 3}))
print(total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}))
print(total_sales({"Book": 1, "Pen": 2, "Notebook": 1}))
