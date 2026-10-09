'''
total = 0

for number in range(100, 301):
    if number % 3 == 0:
        print(number)


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

largest = 0
number = int(input('Enter a number please : '))

while number >= 0:
    
    number = int(input('Enter a number please : '))
    if number < 0:
        print('The biggest number is ')



number_lyst = [2, 5, 1, 7, 8, 10, 2, 4, 3]


def find_largest(Lyst):
    largest = Lyst[0]
    for current_number in Lyst:
        if current_number > largest:
            largest = current_number
    return largest


largest = find_largest(number_lyst)

print(largest)


names = ['Bryan', 'Jonah', 'Landon']


def find_longest(name):
    longest = name[0]
    for current_name in name:
        if len(current_name) > len(longest):
            longest = current_name
    return longest


find_longest(names)
print(find_longest)
'''

cart = {'apples': 2, 'bananas': 7, 'watermelon': 5, 'kiwi': 4}
# food_value = cart
# cart['watermelon'] = cart['watermelon'] + 1


# for key in cart:
#    food_value = cart[key]
#    print(key, cart[key])


def find_most_abundunt_food(grocery_dict):
    largest_qty = 0
    most_abundent_food = ''
    for most_abundent_food in grocery_dict:
        if most_abundent_food > largest_qty:
            largest_qty = most_abundunt_food
    return most_abundent_food


most_abundunt_food = find_most_abundunt_food(cart)

print(most_abundunt_food)
