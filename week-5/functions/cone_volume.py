import math


def cone_volume(r, h):
    volume = math.pi * (r ** 2 * h) / 3
    return int(volume * 100) / 100


r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
print(cone_volume(r, h))
