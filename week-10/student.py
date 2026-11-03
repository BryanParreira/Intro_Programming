class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm studying {self.major}.")

    def study_for_exam(self):
        old_gpa = self.gpa
        self.gpa = min(self.gpa + 0.2, 4.0)
        print(f"I'm hitting the books! My GPA increased from {old_gpa} to {round(self.gpa, 1)}.")


s = Student("Maria", "Computer Science", 3.5)
s.introduce()
s.study_for_exam()
