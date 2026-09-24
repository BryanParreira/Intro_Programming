def pool_time(grade, time):
    if grade == "k" or 1 <= grade <= 3:
        morning = "9 AM"
        afternoon = "1 PM"
    elif 4 <= grade <= 8:
        morning = "10 AM"
        afternoon = "2 PM"
    elif 9 <= grade <= 12:
        morning = "11 AM"
        afternoon = "3 PM"
    else:
        return "unknown"

    if time.lower() == "morning":
        return morning
    elif time.lower() == "afternoon":
        return afternoon
    else:
        return "unknown"


grade = input("Enter your grade (k or 1-12): ").lower()
if grade != "k":
    grade = int(grade)
time = input("Morning or Afternoon? ")
print(pool_time(grade, time))
