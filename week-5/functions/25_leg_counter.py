def leg_counter(chickens, cows, pigs):
    return chickens * 2 + cows * 4 + pigs * 4


chickens = int(input("How many chickens? "))
cows = int(input("How many cows? "))
pigs = int(input("How many pigs? "))
print(leg_counter(chickens, cows, pigs))
