def check_letter(letter):
    if letter in "aeiou":
        return "Vowel"
    else:
        return "Consonant"


letter = input("Enter a single lowercase letter: ")
print(check_letter(letter))
