'''
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i * j, end=" ")
    print()
'''

user_number1 = int(input("Give me a number : "))
user_number2 = int(input("Give me another number : "))
number1 = 1


while number1 <= user_number1:
    number2 = 1
    while number2 <= user_number2:
        print(number1 * number2, end=" ")
        number2 += 1
    number1 += 1
    print("")

class LinkedList:
    def __init__(self):
        pass
    def __iter__(self):
        pass

class string:
    def __init__(self):
        pass
    def __iter__(self):
        pass