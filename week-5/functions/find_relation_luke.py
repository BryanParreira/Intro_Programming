def find_relation(name):
    if name == "Darth Vader":
        return "Father"
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother in law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "Unknown"


name = input("Enter a name: ")
print(find_relation(name))
