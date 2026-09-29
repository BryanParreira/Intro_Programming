def even_numbers(small_num, large_num):
    result = []
    for n in range(small_num, large_num + 1):
        if n % 2 == 0:
            result.append(n)
    return result

print(even_numbers(10, 500))
