health_points = -1

race = input("Enter the race of your character: ")
character_class = input("Enter the class of your character: ")

if race == "Elf":
    if character_class == "Warrior":
        health_points = 150
    elif character_class == "Bard":
        health_points = 75
    elif character_class == "Wizard":
        health_points = 25
elif race == "Ogre":
    if character_class == "Warrior":
        health_points = 200
    elif character_class == "Bard":
        health_points = 100
    elif character_class == "Wizard":
        health_points = 50

print("health_points:", health_points)
