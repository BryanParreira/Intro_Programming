class Course:
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

    def get_course_code(self):
        return self.course_code

    def set_course_code(self, course_code):
        self.course_code = course_code

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_instructor(self):
        return self.instructor

    def set_instructor(self, instructor):
        self.instructor = instructor

    def print_info(self):
        print(f"{self.course_code}: {self.course_name} taught by {self.instructor}")


c = Course("CIS101", "Introduction to programming", "Matt")
c.print_info()
