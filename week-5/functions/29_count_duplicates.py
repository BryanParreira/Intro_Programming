def count_duplicates(num_1, num_2, num_3):
    if num_1 == num_2 and num_2 == num_3:
        return "You entered the same number 3 times"
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        return "You entered the same number 2 times"
    else:
        return "Each number is unique"


num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))
print(count_duplicates(num_1, num_2, num_3))
