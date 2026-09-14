side1 = input("Pick side length 1: ")
side2 = input("Pick side length 2: ")
side3 = input("Pick side length 3: ")

if side1 == side2 and side2 == side3:
    print("equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("isosceles triangle")
else:
    print("scalene triangle")
