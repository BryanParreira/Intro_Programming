def odd_sum(smaller_num, larger_num):
    total = 0
    for number in range(smaller_num, larger_num + 1):
        if number % 2 == 1:
            total = total + number
    return total


smaller_num = int(input("Enter the smaller number: "))
larger_num = int(input("Enter the larger number: "))
print(odd_sum(smaller_num, larger_num))
