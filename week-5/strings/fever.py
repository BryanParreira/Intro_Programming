temp = input("Enter the temperature (like 99F or 37C): ")


def is_fever(temp):
    unit = temp[-1]
    number = float(temp[:-1])
    if unit == "F" or unit == "f":
        return number > 98.6
    else:
        return number > 37


print(is_fever(temp))
