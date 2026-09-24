def get_drink_ID(flavor, capacity):
    return flavor[:3] + str(capacity)


flavor = input("Enter the flavor: ")
capacity = int(input("Enter the capacity: "))
print(get_drink_ID(flavor, capacity))
