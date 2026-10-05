'''
lyst = ["National", "Aeronautics", "Space", "Administration"]


def is_acronym(s, words):
    result = ""
    for i in words:
        result += i[0]
        if result == s:
            return True
        elif result != s:
            return False


print(is_acronym)
print()

'''
lyst = ["National", "Aeronautics", "Space", "Administration"]


def is_acronym(s, words):
    result = ' '
    index = 0
    while s in len(words):
        if s < index[result + 1]:
            return result
    is_acronym(lyst)
    print(result)


lyst = ["National", "Aeronautics", "Space", "Administration"]


def is_acronym(words):
    acronym = ""
    for letter in words:
        if letter:
            acronym += letter[0]
    return acronym


result = is_acronym(lyst)
print(result)
