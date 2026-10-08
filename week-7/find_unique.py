def find_unique(numbers):
    for number in numbers:
        if numbers.count(number) == 1:
            return number


print(find_unique([1, 2, 2, 3, 3, 4, 4]))
print(find_unique([7, 8, 8, 9, 9, 10, 10]))
print(find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9]))
