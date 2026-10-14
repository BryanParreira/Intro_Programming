def descending_order(num1, num2=15, num3=5):
    a, b, c = num1, num2, num3
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return [a, b, c]