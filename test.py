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


# sentence = """Something random that doesnt make any sense."""

data = ['apple', 5, 'banana', True, 2, 3,
        "Something random that doesnt make any sense."]

index = 6
word = ""
while index < len(word):
    print(word)
    index += 1


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



x = 3

x = x * 3
x = x + 1
x = x / 2
x = x ** 3




def name_of_function(zero_or_more_parameters):

    pass


def math_fctn(number):
    number = number * 3
    number = number + 1
    number = number / 2
    number = number ** 3
    print(number)

math_fctn(3)
math_fctn(-2)
math_fctn(10)


n = int(input('give me a number : '))


def even_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print('odd')


even_odd(n)



def make_bigger(num1, num2):
    if num1 < num2:
        num1 += 1
    else:
        num2 += 1
    print(f'{num1 = },{num2 = }')

x = 3
y = 7
make_bigger(x, y)



def is_vowel(letter):
    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True


def word_vowels(word):
    count = 0
    for letter in word:
        if is_vowel(letter):
            count += 1
    print(count)


word_vowels('bananas')
word_vowels('apple')
word1 = 'apple'
word2 = 'bananas'
word3 = 'watermelon'
'''


def even_number(odd, even):
    list = []
    number_list = [10, 15]
    for number_list in range[odd, even]:
        if number_list % 2 == 0:
            list.append(number_list)
        elif number_list % 2 == 1:
            pass
    print(number_list)
