def create_word():
    word = ""
    letter = input("Enter a letter (or type done): ")
    while letter != "done":
        word = word + letter
        letter = input("Enter a letter (or type done): ")
    return word


print(create_word())
