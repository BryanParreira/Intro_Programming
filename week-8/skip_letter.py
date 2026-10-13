
def skip_letter(name):
    result = ''
    for i in range(len(name)):
        if i % 2 == 1:
            result += name[i]
    return result

