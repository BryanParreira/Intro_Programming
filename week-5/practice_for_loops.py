# EXAM PRACTICE - week 5 strings + functions.
# Each run picks 3 RANDOM questions from the whole pool (like the exam).
# Fill in ONLY the 3 functions it tells you about; others stay `pass`.
# Run:  python3 practice_for_loops.py          (new random 3 each time)
#       python3 practice_for_loops.py 7        (same 3 every time, seed 7)
#       python3 practice_for_loops.py all      (test every question)
# Use FOR loops where a FOR hint appears. Only sum_loop/create_word need while.

import random
import sys
from unittest.mock import patch
from contextlib import redirect_stdout
import io


# ---------- STRINGS ----------

def reverse_string(word):
    result = ""
    for letter in word:
        result = letter + result
    print(reverse_string("abc"))
    return result
    """"abc" -> "cba". """
    pass


def first_letters(sentence):
    result = ""
    for letter in sentence:
        if letter.isalpha():
            result += letter
    return result
    """"hello big world" -> "hbw". """
    pass


def last_letters(sentence):
    """"hello big world" -> "ogd". """
    pass


def get_drink_ID(flavor, capacity):
    """First 3 letters of flavor + capacity. ("lemonade", 12) -> "lem12"."""
    pass


def is_fever(temp):
    """temp like "99F" or "37C" (any case unit).
    True if F > 98.6 or C > 37, else False."""
    pass


def is_boiling(temp):
    """temp like "212F" or "100c". True if F >= 212 or C >= 100."""
    pass


def flip_flop(word):
    """Swap first half and last half; middle letter stays if odd length.
    "abcd" -> "cdab", "abcde" -> "decab"."""
    pass


def is_isogram(word):
    """True if no letter repeats. "python" -> True, "hello" -> False.
    FOR: for letter in word: if word.count(letter) > 1 -> return False"""
    pass


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "The strings must be the same length"
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            pass
    """Count positions where letters differ. "cat","cut" -> 1.
    If lengths differ return "The strings must be the same length".
    FOR: for i in range(len(str1)): compare str1[i] and str2[i]"""
    pass


def skip_letter_first(word):
    """Letters at index 0, 2, 4... "abcdef" -> "ace".
    FOR: for i in range(0, len(word), 2)"""
    pass


def skip_letter_second(word):
    for i in range(1, len(word), 2):
        pass
    """Letters at index 1, 3, 5... "abcdef" -> "bdf".
    FOR: for i in range(1, len(word), 2)"""
    pass


def check_letter(letter):
    """Single lowercase letter. Return "Vowel" or "Consonant"."""
    pass


def design_rug(width, length, pattern):
    """Return "Your rug is:" then `length` lines, each pattern repeated
    `width` times. (3, 2, "*") -> "Your rug is:\\n***\\n***".
    FOR: for row in range(length): rug = rug + "\\n" + pattern * width"""
    pass


# ---------- FUNCTIONS: IF / ELIF ----------

def access_rights(user_role):
    """admin -> "full", user -> "limited", guest -> "view",
    else "unknown". Ignore case."""
    pass


def traffic_light(light_color):
    """green -> "Go", yellow -> "Yield", red -> "Stop",
    else "Invalid light color". Ignore case."""
    pass


def serve_coffee(selected_coffee):
    """espresso/latte/cappuccino (ignore case) -> "Here is your latte!"
    else "Sorry, we don't have mocha."  (lowercase name in message)"""
    pass


def find_winner(player1, player2):
    """Rock paper scissors, ignore case.
    "It's a tie!", "Player 1 wins!", or "Player 2 wins!"."""
    pass


def triangle_type(side_1, side_2, side_3):
    """"equilateral", "isosceles", or "scalene"."""
    pass


def count_duplicates(num_1, num_2, num_3):
    """All same -> "You entered the same number 3 times"
    two same -> "You entered the same number 2 times"
    else "Each number is unique"."""
    pass


def highway_directions(highway_num):
    """Valid: 1-999 and last two digits not 00.
    Invalid -> "I-100 is an invalid highway number".
    Odd last-two-digits number -> "I-95 runs north/south",
    even -> "I-10 runs east/west"."""
    pass


def pool_time(grade, time):
    """grade is "k" or int 1-12. time "morning"/"afternoon" (ignore case).
    k-3: 9 AM / 1 PM. 4-8: 10 AM / 2 PM. 9-12: 11 AM / 3 PM.
    Anything else -> "unknown"."""
    pass


def resting_rate(age, athl_goal):
    """Ages 20-39: above average "47-72", below average "73-93".
    40-59: "46-71" / "72-94". 60-79: "45-70" / "71-97".
    Otherwise "unknown". athl_goal is "Above Average"/"Below Average"."""
    pass


# ---------- FUNCTIONS: MATH / LOOPS ----------

def leg_counter(chickens, cows, pigs):
    """chicken 2 legs, cow 4, pig 4. Return total legs."""
    pass


def battery_counter(e_dolls, rc_cars, robo_dogs):
    """dolls 2 batteries, cars 4, dogs 6. Return total."""
    pass


def pyramid_volume(b, h):
    """(b**2 * h) / 3, truncated (not rounded) to 2 decimals."""
    pass


def cone_volume(r, h):
    """pi * r**2 * h / 3, truncated to 2 decimals. Use math.pi."""
    pass


def find_factors(num):
    """List of all factors of num, ascending. 6 -> [1, 2, 3, 6].
    FOR: result = []; for i in range(1, num + 1): if num % i == 0: append"""
    pass


def odd_sum(smaller_num, larger_num):
    """Sum of odd numbers from smaller to larger, inclusive.
    FOR: for n in range(smaller_num, larger_num + 1): if n % 2 == 1"""
    pass


def square_sum(num):
    """1**2 + 2**2 + ... + num**2. If num < 1 return "unknown".
    FOR: for i in range(1, num + 1): total = total + i ** 2"""
    pass


def cube_sum(num):
    """1**3 + 2**3 + ... + num**3. If num < 1 return "unknown".
    FOR: for i in range(1, num + 1): total = total + i ** 3"""
    pass


def hailstone_seq(n):
    """List starting at n. Even -> n//2, odd -> 3n+1, stop at 1 (include 1).
    6 -> [6, 3, 10, 5, 16, 8, 4, 2, 1]."""
    pass


def convert_bronze(bronze_coins):
    """(No loop: use // and %.) 20 bronze = 1 silver, 15 silver = 1 gold.
    Return like "1 gold 2 silver 5 bronze". Skip zero parts.
    0 coins -> "0 bronze"."""
    pass


def sum_loop():
    """(Keep WHILE: unknown number of inputs.) Ask input("Enter an integer: ") repeatedly. Add while number >= 0.
    Stop at a negative number (don't add it). Return total."""
    pass


def create_word():
    """(Keep WHILE: unknown number of inputs.) Ask input() for letters until user types "done".
    Return all letters joined into one word."""
    pass


# =========================================================
# TESTS - don't edit below


def output_even(smaller_num, larger_num):
    """PRINT (not return) each even number, one per line, inclusive.
    (1, 6) prints 2, 4, 6."""
    pass

# =========================================================
# EXAM RUNNER - don't edit below
# =========================================================


CASES = {}  # name -> (kind, func, data)


def add(name, func, cases):
    CASES[name] = ("args", func, cases)


def add_input(name, func, inputs, expected):
    base = name.split(" ")[0]
    CASES.setdefault(base, ("input", func, []))[2].append((inputs, expected))


def check_args(name, func, cases):
    ok = True
    for args, expected in cases:
        try:
            got = func(*args)
        except Exception as e:
            got = "ERROR: " + repr(e)
        if got != expected:
            if ok:
                print("FAIL " + name)
            ok = False
            print("   " + name + str(args) + " -> " + repr(got)
                  + " | expected " + repr(expected))
    if ok:
        print("PASS " + name)


def check_input(name, func, cases):
    ok = True
    for inputs, expected in cases:
        try:
            with patch("builtins.input", side_effect=list(inputs)):
                got = func()
        except Exception as e:
            got = "ERROR: " + repr(e)
        if got != expected:
            if ok:
                print("FAIL " + name)
            ok = False
            print("   " + name + " with inputs " + str(inputs) + " -> "
                  + repr(got) + " | expected " + repr(expected))
    if ok:
        print("PASS " + name)


add("reverse_string", reverse_string, [(("abc",), "cba"), ((
    "",), ""), (("racecar",), "racecar"), (("python",), "nohtyp")])
add("first_letters", first_letters, [
    (("hello big world",), "hbw"), (("a",), "a")])
add("last_letters", last_letters, [
    (("hello big world",), "ogd"), (("a",), "a")])
add("get_drink_ID", get_drink_ID, [
    (("lemonade", 12), "lem12"), (("cola", 8), "col8")])
add("is_fever", is_fever, [(("99F",), True), (("98.6F",), False), ((
    "37C",), False), (("38c",), True), (("97f",), False)])
add("is_boiling", is_boiling, [(("212F",), True), ((
    "211f",), False), (("100C",), True), (("99c",), False)])
add("flip_flop", flip_flop, [(("abcd",), "cdab"), ((
    "abcde",), "decab"), (("a",), "a"), (("ab",), "ba")])
add("is_isogram", is_isogram, [
    (("python",), True), (("hello",), False), (("",), True)])
add("hamming_distance", hamming_distance, [(("cat", "cut"), 1), (("abc", "abc"), 0), ((
    "abc", "xyz"), 3), (("ab", "abc"), "The strings must be the same length")])
add("skip_letter_first", skip_letter_first, [
    (("abcdef",), "ace"), (("abcde",), "ace"), (("a",), "a")])
add("skip_letter_second", skip_letter_second, [
    (("abcdef",), "bdf"), (("abcde",), "bd"), (("a",), "")])
add("check_letter", check_letter, [
    (("a",), "Vowel"), (("z",), "Consonant"), (("u",), "Vowel")])
add("design_rug", design_rug, [
    ((3, 2, "*"), "Your rug is:\n***\n***"), ((2, 3, "ab"), "Your rug is:\nabab\nabab\nabab")])

add("access_rights", access_rights, [(("Admin",), "full"), ((
    "user",), "limited"), (("GUEST",), "view"), (("bob",), "unknown")])
add("traffic_light", traffic_light, [(("Green",), "Go"), ((
    "yellow",), "Yield"), (("RED",), "Stop"), (("blue",), "Invalid light color")])
add("serve_coffee", serve_coffee, [
    (("Latte",), "Here is your latte!"), (("MOCHA",), "Sorry, we don't have mocha.")])
add("find_winner", find_winner, [(("rock", "scissors"), "Player 1 wins!"), (("Paper", "scissors"), "Player 2 wins!"), ((
    "rock", "ROCK"), "It's a tie!"), (("scissors", "paper"), "Player 1 wins!")])
add("triangle_type", triangle_type, [((3, 3, 3), "equilateral"), ((
    3, 3, 4), "isosceles"), ((3, 4, 3), "isosceles"), ((3, 4, 5), "scalene")])
add("count_duplicates", count_duplicates, [((1, 1, 1), "You entered the same number 3 times"), ((
    1, 2, 1), "You entered the same number 2 times"), ((1, 2, 3), "Each number is unique")])
add("highway_directions", highway_directions, [((95,), "I-95 runs north/south"), ((10,), "I-10 runs east/west"), ((100,), "I-100 is an invalid highway number"), ((
    0,), "I-0 is an invalid highway number"), ((1000,), "I-1000 is an invalid highway number"), ((405,), "I-405 runs north/south"), ((110,), "I-110 runs east/west")])
add("pool_time", pool_time, [(("k", "Morning"), "9 AM"), ((3, "afternoon"), "1 PM"), ((4, "morning"), "10 AM"), ((
    8, "Afternoon"), "2 PM"), ((12, "morning"), "11 AM"), ((9, "afternoon"), "3 PM"), ((13, "morning"), "unknown"), ((5, "night"), "unknown")])
add("resting_rate", resting_rate, [((25, "Above Average"), "47-72"), ((39, "below average"), "73-93"), ((40, "Above Average"), "46-71"), ((59, "Below Average"),
    "72-94"), ((60, "above average"), "45-70"), ((79, "Below Average"), "71-97"), ((19, "Above Average"), "unknown"), ((30, "average"), "unknown")])

add("leg_counter", leg_counter, [
    ((1, 1, 1), 10), ((0, 0, 0), 0), ((3, 2, 1), 18)])
add("battery_counter", battery_counter, [((1, 1, 1), 12), ((2, 0, 3), 22)])
add("pyramid_volume", pyramid_volume, [((3, 4), 12.0), ((2.5, 7), 14.58)])
add("cone_volume", cone_volume, [((3, 5), 47.12), ((1, 1), 1.04)])
add("find_factors", find_factors, [((6,), [1, 2, 3, 6]), ((
    7,), [1, 7]), ((1,), [1]), ((12,), [1, 2, 3, 4, 6, 12])])
add("odd_sum", odd_sum, [((1, 10), 25),
    ((2, 2), 0), ((3, 3), 3), ((4, 9), 21)])
add("square_sum", square_sum, [((3,), 14), ((1,), 1), ((0,), "unknown")])
add("cube_sum", cube_sum, [((3,), 36), ((1,), 1), ((-2,), "unknown")])
add("hailstone_seq", hailstone_seq, [
    ((6,), [6, 3, 10, 5, 16, 8, 4, 2, 1]), ((1,), [1])])
add("convert_bronze", convert_bronze, [((0,), "0 bronze"), ((5,), "5 bronze"), ((20,), "1 silver"), ((
    300,), "1 gold"), ((345,), "1 gold 2 silver 5 bronze"), ((25,), "1 silver 5 bronze")])
add_input("sum_loop", sum_loop, ["5", "10", "3", "-1"], 18)
add_input("sum_loop (first negative)", sum_loop, ["-4"], 0)
add_input("create_word", create_word, ["c", "a", "t", "done"], "cat")
add_input("create_word (immediate done)", create_word, ["done"], "")


def printed(func, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        func(*args)
    return buf.getvalue()


add("output_even", lambda a, b: printed(output_even, a, b),
    [((1, 6), "2\n4\n6\n"), ((3, 3), "")])


# ---------- pick questions ----------
arg = sys.argv[1] if len(sys.argv) > 1 else ""
names = list(CASES)
if arg == "all":
    picked = names
else:
    if arg:
        random.seed(arg)
    picked = random.sample(names, 3)

print("=" * 60)
print("YOUR " + str(len(picked)) + " QUESTIONS: " + ", ".join(picked))
print("=" * 60)
for name in picked:
    doc = globals()[name].__doc__ or ""
    print("\n" + name + ":\n  " + doc.strip().replace("\n", "\n  "))
print("\n" + "-" * 60)
for name in picked:
    kind, func, data = CASES[name]
    if kind == "args":
        check_args(name, func, data)
    else:
        check_input(name, func, data)
