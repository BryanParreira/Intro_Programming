'''
user_word = input("Enter a word: ")

result = ""

for index in range(1, len(user_word), 2):
    result = result + user_word[index]
    #result = result + user_word

print(result)
'''
'''
word = input('Give me a word :')
count = 0
for letter in word:
    if count % 2 == 0:
        print(letter)
    count = count + 1
'''


user_word = input("Give me a word: ")
index = 0

while index < len(user_word):
    if index % 2 == 0:
        print(user_word[index])
    index += 1
