'''
total = 0

for number in range(100, 301):
    if number % 3 == 0:
        print(number)
'''
total = 0
count = 0

number = int(input('Enter a number please : '))

while number != 0:
    total += number
    count += 1
    number = int(input('Enter a number please : '))
else:
    if count > 0:
        print(total / count)
