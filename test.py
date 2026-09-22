'''
start = 5
end = 32

for number in range(start, end):
    if number % 2 == 0:
        print(number)
'''
'''
number = 5
while number <= 32:
    if number % 2 == 0:
        print(number)
    number += 1
'''


# for number in range(1, 10+1):
#    print(number)

'''
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

for number in range(lower_bound, upper_bound + 1):
    print(number)
'''
'''
for number in range(4, 37+1):
    if number % 2 == 1:
        print(number)
'''
'''
for number in range(10):
    print(number)

word = "apple"

for index in range(len(word)):
    print(word[index])
'''
'''
word = 'apples and bananas are good'
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word:
    if letter in vowels:
        print(letter)
'''

'''
sentence = """Something random that doesnt make any sense."""

word = ""
for letter in sentence:
    if letter == " ":
        print(word)
        word = ""
    elif letter == ".":
        print(word)
        word = ""
    else:
        word += letter
'''

# sentence = """Something random that doesnt make any sense."""

data = ['apple', 5, 'banana', True, 2, 3,
        "Something random that doesnt make any sense."]

index = 6
word = ""
while index < len(word):
    print(word)
    index += 1

'''
sentence = 'Something random that doesnt make any sense.'

lyst = []
word = ""
for letter in sentence:
    if letter == " " or letter == ".":
        lyst.append(word)
        word = ""
    else:
        word += letter

print(lyst)
'''
