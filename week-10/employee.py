class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def greeting(self):
        print(f"Hello. My name is {self.name}. I'm the {self.title}.")

    def request_raise(self):
        new_salary = self.salary * 1.06
        print(f"I'm currently making $ {self.salary}. I'd like new salary of $ {new_salary}.")


e = Employee("Eugene", "CEO", 100)
e.greeting()
e.request_raise()
