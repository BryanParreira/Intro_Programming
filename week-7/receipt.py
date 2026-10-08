# (a)
receipt = {}
receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3

# (b)
total = 0
for item in receipt:
    total += receipt[item]

print(f"Total cost: ${total}")
