age = int(input("Enter your age: "))
goal = input("Enter your athleticism goal: ")

if 20 <= age <= 39:
    if goal == "Above Average":
        print("Your resting heart rate should be between 47-72.")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 73-93.")
elif 40 <= age <= 59:
    if goal == "Above Average":
        print("Your resting heart rate should be between 46-71.")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 72-94.")
elif 60 <= age <= 79:
    if goal == "Above Average":
        print("Your resting heart rate should be between 45-70.")
    elif goal == "Below Average":
        print("Your resting heart rate should be between 71-97.")
