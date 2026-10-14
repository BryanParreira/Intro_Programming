def is_two_digit_number(num):
    return -99 <= num <= -10 or 10 <= num <= 99

def report_two_digit_numbers(lst):
    two_digits = []
    for num in lst:
        if is_two_digit_number(num):
            two_digits.append(num)
    return two_digits