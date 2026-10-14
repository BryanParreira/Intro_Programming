def ascending_order(num1, num2=5, num3=25):
    a, b, c = num1, num2, num3
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return [a, b, c]