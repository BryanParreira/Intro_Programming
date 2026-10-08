def total_donations(donations):
    total = 0
    for donor in donations:
        total += donations[donor]
    return total


print(total_donations({"John": 100, "Sarah": 200, "Mike": 50}))
print(total_donations({"Anna": 500, "Tom": 1000, "Jerry": 1500}))
print(total_donations({"Chris": 25, "Alex": 30, "Morgan": 45}))
