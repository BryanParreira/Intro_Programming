def cube_sum(num):
    if num < 1:
        return "unknown"
    total = 0
    for i in range(1, num + 1):
        total = total + i ** 3
    return total


num = int(input("Enter an integer: "))
print(cube_sum(num))
