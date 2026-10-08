def high_earners(employee_salaries, salary):
    earners = []
    for name, amount in employee_salaries.items():
        if amount > salary:
            earners.append(name)
    return earners


print(high_earners({"Alice": 50000, "Bob": 75000, "Charlie": 100000}, 60000))
print(high_earners({"David": 30000, "Emma": 45000, "Frank": 50000}, 40000))
print(high_earners({"George": 25000, "Hannah": 27000, "Ian": 29000}, 30000))
