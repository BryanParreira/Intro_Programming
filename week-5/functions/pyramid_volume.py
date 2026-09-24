def pyramid_volume(b, h):
    volume = (b ** 2 * h) / 3
    return int(volume * 100) / 100  # keep 2 decimal places


b = float(input("Enter the base edge: "))
h = float(input("Enter the height: "))
print(pyramid_volume(b, h))
