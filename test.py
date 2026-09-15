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

word = 'apples and bananas are good'
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in word:
    if letter in vowels:
        print(letter)
