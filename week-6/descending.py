def descending_order(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        largest = num_1
        if num_2 >= num_3:
            middle = num_2
            smallest = num_3
        else:
            middle = num_3
            smallest = num_2
    elif num_2 >= num_1 and num_2 >= num_3:
        largest = num_2
        if num_1 >= num_3:
            middle = num_1
            smallest = num_3
        else:
            middle = num_3
            smallest = num_1
    else:
        largest = num_3
        if num_1 >= num_2:
            middle = num_1
            smallest = num_2
        else:
            middle = num_2
            smallest = num_1
    return [largest, middle, smallest]

print(descending_order(2, 3, 1))
print(descending_order(10, 1, 25))
print(descending_order(2, 45, 4))
