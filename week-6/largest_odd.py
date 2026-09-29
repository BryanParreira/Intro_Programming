def largest_odd(numbers):
    result = -1
    for n in numbers:
        if n % 2 != 0 and n > result:
            result = n
    return result

print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_odd([2, 4, 6, 8]))
print(largest_odd([0, 19, 18973623]))
