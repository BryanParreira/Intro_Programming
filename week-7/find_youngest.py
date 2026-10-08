def find_youngest(people):
    youngest_age = None
    youngest_person = None

    for name, age in people.items():
        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_person = name

    return youngest_person


print(find_youngest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))
print(find_youngest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33}))
print(find_youngest({"Ethan": 25, "Lucas": 30, "Mia": 29}))
