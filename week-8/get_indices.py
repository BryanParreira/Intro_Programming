def get_indices(lst, value=0):
    indices = []
    for i in range(len(lst)):
        if lst[i] == value:
            indices.append(i)
    return indices