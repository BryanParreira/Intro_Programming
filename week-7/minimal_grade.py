grade = {'Math': 80, 'Geography': 50, 'History': 34}


def lowest(grade):
    lowest_grade_value = None
    lowest_class = None

    for class_name, grade_value in grade.items():
        if lowest_grade_value is None or grade_value < lowest_grade_value:
            lowest_grade_value = grade_value
            lowest_class = class_name

    return lowest_class, lowest_grade_value


lowest_class, lowest_grade = lowest(grade)
print(f'The lowest grade you have is: {lowest_grade} in {lowest_class}')
