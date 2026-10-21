def count_duplicates(num_1, num_2, num_3):
    if num_1 == num_2 == num_3:
        return "You entered the same number 3 times"
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        return "You entered the same number 2 times"
    else:
        return "Each number is unique"

# Test the function with a sample input

print(count_duplicates(2, 3, 2)) # Expected output: "You entered the same number 2 times"
print(count_duplicates(4, 4, 4)) # Expected output: "You entered the same number 3 times"
print(count_duplicates(1, 2, 3)) # Expected output: "Each number is unique"
