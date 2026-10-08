def get_names(names):
    students = []
    for tech_id in names:
        students.append(names[tech_id])
    return students


print(get_names({"01475": "Steve", "87469": "Alice", "654123": "Bob"}))
print(get_names({"ID1": "John", "ID2": "Emma", "ID3": "Liam"}))
print(get_names({}))
