family_members = ["Darth Vader", "Leia", "Han", "R2D2"]
relationships = ["father", "sister", "brother-in-law", "droid"]

user_input = input("Enter a family member's name: ")

if user_input not in family_members:
    print("Unknown")
elif user_input == "Darth Vader":
    print(
        f"Darth Vader is a member of the family. It is your {relationships[0]}.")
elif user_input == "Leia":
    print(f"Leia is a member of the family. It is your {relationships[1]}.")
elif user_input == "Han":
    print(f"Han is a member of the family. It is your {relationships[2]}.")
elif user_input == "R2D2":
    print(f"R2D2 is a member of the family. It is your {relationships[3]}.")
