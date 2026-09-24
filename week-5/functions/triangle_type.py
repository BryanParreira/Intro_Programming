def triangle_type(side_1, side_2, side_3):
    if side_1 == side_2 and side_2 == side_3:
        return "equilateral"
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        return "isosceles"
    else:
        return "scalene"


side_1 = float(input("Enter side 1: "))
side_2 = float(input("Enter side 2: "))
side_3 = float(input("Enter side 3: "))
print(triangle_type(side_1, side_2, side_3))
