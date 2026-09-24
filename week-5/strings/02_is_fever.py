def is_fever(temp):
    unit = temp[-1].upper()
    number = float(temp[:-1])
    if unit == "F":
        return number > 98.6
    else:
        return number > 37


temp = input("Enter the temperature (like 99F or 37C): ")
print(is_fever(temp))
