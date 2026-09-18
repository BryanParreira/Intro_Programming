larger = int(input("Enter the larger integer: "))
smaller = int(input("Enter the smaller integer: "))

count = 0

while larger / 2 > smaller:
    larger = larger / 2
    count = count + 1

print("Number of times larger can be halved:", count)
