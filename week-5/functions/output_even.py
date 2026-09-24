def output_even(smaller_num, larger_num):
    for number in range(smaller_num, larger_num + 1):
        if number % 2 == 0:
            print(number)


smaller_num = int(input("Enter the smaller number: "))
larger_num = int(input("Enter the larger number: "))
output_even(smaller_num, larger_num)
