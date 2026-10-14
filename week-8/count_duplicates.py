def count_duplicates(num1=0, num2=0, num3=0):
    unique_count = len(set([num1, num2, num3]))
    if unique_count == 3:
        return "Each number is unique"
    elif unique_count == 2:
        return "There are 2 of the same number"
    return "There are 3 of the same number"