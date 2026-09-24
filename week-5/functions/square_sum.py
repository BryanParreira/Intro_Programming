def square_sum(num):
    if num < 1:
        return "unknown"
    total = 0
    for i in range(1, num + 1):
        total = total + i ** 2
    return total


num = int(input("Enter an integer: "))
print(square_sum(num))
