class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"


class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget

    def set_budget(self, budget):
        self.budget = budget

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_staff_list(self):
        for employee in self.employees:
            print(employee)

    def is_large(self):
        return len(self.employees) >= 10

    def __str__(self):
        return f"{self.dept_name} (budget ${self.budget}, {len(self.employees)} employees)"


dept = Department("Engineering", 500000)
dept.add_employee(Employee("Sam", "Developer"))
dept.add_employee(Employee("Lee", "Manager"))
print(dept)
dept.show_staff_list()
print(dept.is_large())  # False
