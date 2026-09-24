def resting_rate(age, athl_goal):
    if 20 <= age <= 39:
        above = "47-72"
        below = "73-93"
    elif 40 <= age <= 59:
        above = "46-71"
        below = "72-94"
    elif 60 <= age <= 79:
        above = "45-70"
        below = "71-97"
    else:
        return "unknown"

    goal = athl_goal.lower()
    if goal == "above average":
        return above
    elif goal == "below average":
        return below
    else:
        return "unknown"


age = int(input("Enter your age: "))
athl_goal = input("Enter your athletic goal (Above Average or Below Average): ")
print(resting_rate(age, athl_goal))
