def is_isogram(word):
    seen = []
    for letter in word.lower():
        if letter in seen:
            return False
        seen.append(letter)
    return True


print(is_isogram("algorism"))
print(is_isogram("password"))
print(is_isogram("consecutive"))
