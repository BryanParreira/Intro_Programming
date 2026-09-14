grade = input("Enter your grade: ")
time_choice = input("Enter Morning OR Afternoon: ")

if grade == "k":
    grade_num = 0
else:
    grade_num = int(grade)

if 0 <= grade_num <= 3:
    if time_choice == "Morning":
        print("The pool is open at 9 AM.")
    elif time_choice == "Afternoon":
        print("The pool is open at 1 PM.")
elif 4 <= grade_num <= 8:
    if time_choice == "Morning":
        print("The pool is open at 10 AM.")
    elif time_choice == "Afternoon":
        print("The pool is open at 2 PM.")
elif 9 <= grade_num <= 12:
    if time_choice == "Morning":
        print("The pool is open at 11 AM.")
    elif time_choice == "Afternoon":
        print("The pool is open at 3 PM.")
