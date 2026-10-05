lyst = ["National", "Aeronautics", "Space", "Administration"]


def is_acronym(s, words):
    result = ""
    for i in words:
        result += i[0]
        if result == s:
            return True
        elif result != s:
            return False


print(is_acronym("Nasa").lyst)
print()
