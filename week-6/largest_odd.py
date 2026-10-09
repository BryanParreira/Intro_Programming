def largest_odd(numbers):
    result = -1
    n = numbers
    while n <= numbers:
        if n % 2 == 0:
            return result
        n += 1
    return n


print(largest_odd([3, 5, 7, 11]))
