def find_relation(name=""):
    relations = {
        "Darth Vader": "Father",
        "Leia": "Sister",
        "Han": "Brother in law",
        "R2D2": "Droid"
    }
    return relations.get(name, "Unknown")