def skip_letter(word):
    result = ""
    for index in range(0, len(word), 2):
        result = result + word[index]
    return result


word = input("Enter a word: ")
print(skip_letter(word))
