def highway_directions(highway_num):
    # valid numbers are 1-999, and the last two digits can't be 00
    if highway_num < 1 or highway_num > 999 or highway_num % 100 == 0:
        return "I-" + str(highway_num) + " is an invalid highway number"

    primary = highway_num % 100
    if primary % 2 == 1:
        return "I-" + str(highway_num) + " runs north/south"
    else:
        return "I-" + str(highway_num) + " runs east/west"


highway_num = int(input("Enter a highway number: "))
print(highway_directions(highway_num))
