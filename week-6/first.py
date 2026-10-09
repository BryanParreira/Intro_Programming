name = input('give me a name: ')


def skip_letter(name):
    result = ''
    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i]
    return result


print(skip_letter(name))
