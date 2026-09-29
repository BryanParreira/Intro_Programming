def largest_even(numbers):
    result = -1
    for n in numbers:
        if n % 2 == 0 and n > result:
            result = n
    return result

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))
