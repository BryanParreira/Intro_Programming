# FOR loop practice. Use ONLY `for` loops (no while). Run: python3 practice_for_loops.py
# Forms:  for letter in word   |   for word in s.split()
#         for i in range(len(s))   |   for i in range(1, n + 1)
#         for i in range(start, len(s), 2)


from contextlib import redirect_stdout
import io


def reverse_string(word):
    result = " "
    for letter in word:
        result = letter + result
    return result


print(reverse_string("abc"))


def first_letters(sentence):
    result = ""
    for word in sentence.split():
        result += word[0]
    return result


print(first_letters("hello big world"))


def last_letters(sentence):
    """"hello big world" -> "ogd". Hint: word[-1]"""
    pass


def count_vowels(word):
    """"banana" -> 3. Hint: if letter in "aeiou": count = count + 1"""
    pass


def skip_letter_first(word):
    """"abcdef" -> "ace". Hint: range(0, len(word), 2)"""
    pass


def skip_letter_second(word):
    """"abcdef" -> "bdf". Hint: range(1, len(word), 2)"""
    pass


def hamming_distance(str1, str2):
    """Count positions that differ. "cat","cut" -> 1.
    Different length -> "The strings must be the same length".
    Hint: for i in range(len(str1)): str1[i] != str2[i]"""
    pass


def is_isogram(word):
    """True if no letter repeats. Hint: word.count(letter) > 1 -> return False"""
    pass


def double_letters(word):
    """Each letter twice. "abc" -> "aabbcc"."""
    pass


def remove_spaces(sentence):
    """"a b c" -> "abc"."""
    pass


def design_rug(width, length, pattern):
    """(3, 2, "*") -> "Your rug is:\\n***\\n***".
    Hint: for row in range(length): rug = rug + "\\n" + pattern * width"""
    pass


def odd_sum(smaller_num, larger_num):
    """Sum of odds from smaller to larger inclusive. (1, 10) -> 25."""
    pass


def square_sum(num):
    """1**2 + ... + num**2. num < 1 -> "unknown". 3 -> 14."""
    pass


def cube_sum(num):
    """1**3 + ... + num**3. num < 1 -> "unknown". 3 -> 36."""
    pass


def find_factors(num):
    """6 -> [1, 2, 3, 6]. Hint: if num % i == 0: result.append(i)"""
    pass


def count_evens(smaller_num, larger_num):
    """How many even numbers from smaller to larger inclusive. (1, 10) -> 5."""
    pass


def factorial(n):
    """5 -> 120 (1*2*3*4*5). 0 -> 1."""
    pass


def multiples(n, count):
    """First `count` multiples of n as a list. (3, 4) -> [3, 6, 9, 12]."""
    pass


def output_even(smaller_num, larger_num):
    """PRINT (not return) each even number, one per line, inclusive."""
    pass


# ====================== TESTS - don't edit below ======================


def run(name, func, cases):
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
            print("   " + name + str(args) + " -> " +
                  repr(got) + " | expected " + repr(expected))
    if ok:
        print("PASS " + name)


run("reverse_string", reverse_string, [
    (("abc",), "cba"), (("",), ""), (("python",), "nohtyp")])
run("first_letters", first_letters, [
    (("hello big world",), "hbw"), (("a",), "a")])
run("last_letters", last_letters, [
    (("hello big world",), "ogd"), (("a",), "a")])
run("count_vowels", count_vowels, [
    (("banana",), 3), (("xyz",), 0), (("aeiou",), 5)])
run("skip_letter_first", skip_letter_first, [
    (("abcdef",), "ace"), (("abcde",), "ace"), (("a",), "a")])
run("skip_letter_second", skip_letter_second, [
    (("abcdef",), "bdf"), (("abcde",), "bd"), (("a",), "")])
run("hamming_distance", hamming_distance, [(("cat", "cut"), 1), (("abc", "abc"), 0), ((
    "abc", "xyz"), 3), (("ab", "abc"), "The strings must be the same length")])
run("is_isogram", is_isogram, [
    (("python",), True), (("hello",), False), (("",), True)])
run("double_letters", double_letters, [(("abc",), "aabbcc"), (("",), "")])
run("remove_spaces", remove_spaces, [(("a b c",), "abc"), (("  x ",), "x")])
run("design_rug", design_rug, [
    ((3, 2, "*"), "Your rug is:\n***\n***"), ((2, 3, "ab"), "Your rug is:\nabab\nabab\nabab")])
run("odd_sum", odd_sum, [((1, 10), 25),
    ((2, 2), 0), ((3, 3), 3), ((4, 9), 21)])
run("square_sum", square_sum, [((3,), 14), ((1,), 1), ((0,), "unknown")])
run("cube_sum", cube_sum, [((3,), 36), ((1,), 1), ((-2,), "unknown")])
run("find_factors", find_factors, [
    ((6,), [1, 2, 3, 6]), ((7,), [1, 7]), ((12,), [1, 2, 3, 4, 6, 12])])
run("count_evens", count_evens, [((1, 10), 5), ((2, 2), 1), ((3, 3), 0)])
run("factorial", factorial, [((5,), 120), ((0,), 1), ((1,), 1), ((3,), 6)])
run("multiples", multiples, [
    ((3, 4), [3, 6, 9, 12]), ((5, 1), [5]), ((2, 0), [])])


def printed(func, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        func(*args)
    return buf.getvalue()


run("output_even", lambda a, b: printed(output_even, a, b),
    [((1, 6), "2\n4\n6\n"), ((3, 3), "")])
