class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f"{self.name} ({self.major})"


class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []  # starts with no students

    def get_number(self):
        return self.course_number

    def set_number(self, course_number):
        self.course_number = course_number

    def add_student(self, student):
        self.students.append(student)

    def show_student_enrollment(self):
        for student in self.students:
            print(student)

    def __str__(self):
        return f"{self.course_number}: {self.course_name} ({len(self.students)} students)"


course = Course("Introduction to Programming", "CIS101")
course.add_student(Student("Maria", "Computer Science"))
course.add_student(Student("Alex", "Math"))
print(course)
course.show_student_enrollment()
