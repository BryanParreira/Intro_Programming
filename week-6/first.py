'''
name = input('give me a name: ')
index = 0

def skip_letter(name):
    for letter in len(name):
        if letter % 2 == 0:
            letter.append(name)
skip_letter(name)
'''

name = input('give me a name: ')

def skip_letter(name):
    result = ''
    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i]
    return result

print(skip_letter(name))
