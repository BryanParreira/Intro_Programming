people = ({"Koda": 30, 'Bryan': 23, 'Ana': 24})


def find_oldest(people):
    oldest_age = -1
    oldest_person = None

    for name, age in people.items():
        if age > oldest_age:
            oldest_age = age
            oldest_person = name

    return oldest_person


oldest = find_oldest(people)
print(f"The oldest person is: {oldest}")
