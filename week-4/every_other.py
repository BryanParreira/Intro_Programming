user_word = input("Enter a word: ")

result = ""

for i in range(1, len(user_word), 2):
    result = result + user_word[i]

print(result)
