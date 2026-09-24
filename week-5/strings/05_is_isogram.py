def is_isogram(word):
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True


word = input("Enter a word: ")
print(is_isogram(word))
