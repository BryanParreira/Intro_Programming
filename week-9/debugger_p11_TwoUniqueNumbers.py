def return_unique(numbers):
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    unique_numbers = []
    for number, count in counts.items():
        if count == 1:
            unique_numbers.append(number)

    return unique_numbers


# Test the function with a sample input
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6])) # Expected output: [9, 7]
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])) # Expected output: [2, 1]
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])) # Expected output: [5, 6]
