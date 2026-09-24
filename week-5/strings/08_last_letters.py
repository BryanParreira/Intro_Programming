def last_letters(sentence):
    result = ""
    for word in sentence.split():
        result = result + word[-1]
    return result


sentence = input("Enter a sentence: ")
print(last_letters(sentence))
