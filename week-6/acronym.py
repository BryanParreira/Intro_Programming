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


def is_acronym(words):
    acronym = ""
    index = 0
    while index < len(words):
        word = words[index]
        if word:
            acronym += word[0]
        index += 1
    return acronym


words = ["Apple", 'Orange']
result = is_acronym(words)
print(result)
