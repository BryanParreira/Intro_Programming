def odd_numbers(small_num, large_num):
    result = []
    n = small_num
    while n <= large_num:
        if n % 2 == 1:
            result.append(n)
        n += 1
    return result


print(odd_numbers(20, 80))
