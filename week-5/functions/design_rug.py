def design_rug(width, length, pattern):
    rug = "Your rug is:"
    for row in range(length):
        rug = rug + "\n" + pattern * width
    return rug


width = int(input("Enter a width: "))
length = int(input("Enter a length: "))
pattern = input("Enter a pattern: ")
print(design_rug(width, length, pattern))
