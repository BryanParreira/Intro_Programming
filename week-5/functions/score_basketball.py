def total_score(two_pointers, three_pointers):
    return two_pointers * 2 + three_pointers * 3


two_pointers = int(input("Enter the number of two-pointers: "))
three_pointers = int(input("Enter the number of three-pointers: "))
print(total_score(two_pointers, three_pointers))
