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
