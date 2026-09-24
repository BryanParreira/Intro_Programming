def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "The strings must be the same length"
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance = distance + 1
    return distance


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(hamming_distance(str1, str2))
