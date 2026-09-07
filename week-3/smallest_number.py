first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number < second_number and first_number < third_number:
    print(f"The smallest number is: {first_number}")
elif second_number < first_number and second_number < third_number:
    print(f"The smallest number is: {second_number}")
else:
    print(f"The smallest number is: {third_number}")
