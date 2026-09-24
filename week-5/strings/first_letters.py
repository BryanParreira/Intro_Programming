def first_letters(sentence):
    result = ""
    for word in sentence.split():
        result = result + word[0]
    return result


sentence = input("Enter a sentence: ")
print(first_letters(sentence))
