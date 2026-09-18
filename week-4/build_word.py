word = ""

letter = input("Enter a letter (or type done): ")

while letter != "done":
    word = word + letter
    letter = input("Enter a letter (or type done): ")

print(word)
