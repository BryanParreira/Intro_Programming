def count_repetitions(elements):
    counts = {}
    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts


print(count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]))
print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]))
print(count_repetitions(["Infinity", "null", "Infinity", "null", "null"]))
