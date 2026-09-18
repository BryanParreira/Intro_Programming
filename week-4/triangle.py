height = int(input("Enter a height: "))

print()
print("Here is a triangle of height", str(height) + ":")

for row in range(1, height + 1):
    print("*" * row)
