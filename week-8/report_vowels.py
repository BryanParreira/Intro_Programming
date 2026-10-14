def is_vowel(letter):
    return letter.lower() in ['a', 'e', 'i', 'o', 'u']

def report_vowels(text):
    vowels = []
    for char in text:
        if is_vowel(char):
            vowels.append(char)
    return vowels