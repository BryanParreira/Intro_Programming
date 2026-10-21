def flip_flop(word):
    length = len(word)
    middle = length // 2

    if length % 2 == 0:
        return word[middle:] + word[:middle]
    else:
        return word[middle + 1:] + word[middle] + word[:middle]

# Test the function with a sample input
print(flip_flop("abcd")) # Expected output: "cdab" (that is, cd then ab ... even length)
print(flip_flop("grapes")) # Expected output: "pesgra" (that is, pes then gra ... even length)
print(flip_flop("abcde")) # Expected output: "decab" (that is, de then c then ab ... odd length)
print(flip_flop("cranberries")) # Expected output: "rriesecranb" (that is, rries then e then cranb ... odd length)

