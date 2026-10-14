def is_negative(num):
    return num < 0

def is_odd(num):
    return num % 2 != 0

def report_negative_odds(lst):
    neg_odds = []
    for num in lst:
        if is_negative(num) and is_odd(num):
            neg_odds.append(num)
    return neg_odds