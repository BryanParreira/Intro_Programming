def list_of_multiples(num, length=5):
    multiples = []
    for i in range(1, length + 1):
        multiples.append(num * i)
    return multiples