a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a < b:
    temp = a
    a = b
    b = temp
if b < c:
    temp = b
    b = c
    c = temp
if a < b:
    temp = a
    a = b
    b = temp

print(f"{a}, {b}, {c}")
