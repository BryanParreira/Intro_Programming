def add_lists(lyst1, lyst2):
    result = []
    for i in range(len(lyst1)):
        result.append(lyst1[i] + lyst2[i])
    return result

print(add_lists([1, 3, 3, 1], [4, 3, 6, 1]))
print(add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6]))
print(add_lists([1, 2], [-1, 1]))
