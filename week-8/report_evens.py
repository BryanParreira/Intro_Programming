def is_even(num):
    return num % 2 == 0

def report_evens(lst):
    evens = []
    for num in lst:
        if is_even(num):
            evens.append(num)
    return evens