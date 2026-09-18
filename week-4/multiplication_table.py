a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

print()
print("The multiplication table is:")

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i * j, end="\t")
    print()
