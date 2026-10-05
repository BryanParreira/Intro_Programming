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



def even_number(odd, even):
    list = []
    for number in range(odd, even):
        if number % 2 == 0:
            list.append(number)
        # elif number % 2 == 1:
         #   pass
    print(list)


even_number(10, 15)



lyst1 = ['a', 'b', 'c']
lyst2 = lyst1
lyst3 = []

for element in lyst1:
    lyst3.append(element)

lyst4 = []

index = 0
while index < len(lyst1):
    lyst4.append(lyst1[index])
    index += 1
print(lyst4)


for element in lyst1:
    lyst4.append(element)



lyst = ['Bryan', 'Landon', 'Wyatt', 'Jonah', 'Matt']


def new_lyst(contain, doesnt):
    for name in range(contain, doesnt):
        if len(name) >= 5:




def new_lys


total = 0
for i in range(1, 6, 2):
    total += 1
print(total)



def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "The strings must be the same length"
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance = distance + 1
    return distance


print(hamming_distance("cat", "cut"))   # 1
print(hamming_distance("ab", "abc"))    # The strings must be the same length



count = 0
for n in range(50, 517):
    if n % 2 == 1:
        count += 1

print(count)


total = 0

number = int(input('Give me a integer'))

while number >= 0:
    total += number
    number = int(input('Give me another integer: '))
print(total)

r = int(input('give me a number: '))
c = int(input('give me a number: '))

for row in range(r):
    for col in range(c):
        print(col * row, end=" ")
    print()
'''
