width = int(input("Enter a width: "))
length = int(input("Enter a length: "))
pattern = input("Enter a pattern: ")

print()
print("Your rug is:")

for row in range(length):
    print(pattern * width)
