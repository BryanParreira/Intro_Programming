def flip_flop(word):
    half = len(word) // 2
    first_half = word[:half]
    middle = word[half:len(word) - half]  # empty if length is even
    second_half = word[len(word) - half:]
    return second_half + middle + first_half


word = input("Enter a word: ")
print(flip_flop(word))
