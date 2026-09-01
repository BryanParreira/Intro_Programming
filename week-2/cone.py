from math import pi

radius = input("Enter the radius of the cone: ")
height = input("Enter the height of the cone: ")

print(
    f"The volume of the cone is {(1/3) * pi * (int(radius) ** 2) * int(height):.2f}")
