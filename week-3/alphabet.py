vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

input_letter = input("Enter a letter: ")

if input_letter in vowels:
    print(f"Correct,{input_letter} is a vowel.")
elif input_letter in consonants:
    print(f"Correct,{input_letter} is a consonant.")
else:
    print("Please enter a valid letter.")
