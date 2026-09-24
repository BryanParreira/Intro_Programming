def find_relation(name):
    if name == "Moriarty":
        return "Archenemy"
    elif name == "Watson":
        return "Best Friend"
    elif name == "Mrs. Hudson":
        return "Landlady"
    elif name == "Inspector Lestrade":
        return "Detective"
    else:
        return "Unknown"


name = input("Enter a name: ")
print(find_relation(name))
