def is_boiling(temp):
    unit = temp[-1].upper()
    number = float(temp[:-1])
    if unit == "F":
        return number >= 212
    else:
        return number >= 100


temp = input("Enter the temperature (like 212F or 100C): ")
print(is_boiling(temp))
