from math import pi

height = input("Enter the height of the cylinder: ")
radius = input("Enter the radius of the cylinder: ")

print(
    f"The volume of the cylinder is {pi * (int(radius) ** 2) * int(height):.2f}")
