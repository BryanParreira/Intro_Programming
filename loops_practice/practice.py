"""
LOOPS PRACTICE — for loops, while loops, functions, strings, lists

HOW TO USE
    1. Pick an exercise. Replace `pass` with your code.
    2. Run the checker from this folder:
           python3 check.py         -> checks everything
           python3 check.py 7       -> checks only exercise 7
    3. Stuck? Look in solutions.py — but try for at least 10 minutes first!

RULES
    - Each exercise says which loop to use (for / while). The checker enforces it.
    - Some exercises ban shortcuts like sum(), max(), .split(), [::-1].
      The point is to build them yourself with loops.
    - Always RETURN the answer. Don't just print it.
"""


# =====================================================================
# LEVEL 1 — for loops + range()
# =====================================================================

def ex1_count_up(n):
    """Use a FOR loop. Return a list of numbers from 1 to n (inclusive).
    count_up(5) -> [1, 2, 3, 4, 5]
    """
    pass


def ex2_sum_to(n):
    """Use a FOR loop. Return 1 + 2 + ... + n.  No sum().
    sum_to(4) -> 10
    """
    pass


def ex3_evens_between(start, end):
    """Use a FOR loop. Return a list of even numbers from start to end (inclusive).
    evens_between(5, 12) -> [6, 8, 10, 12]
    """
    pass


def ex4_times_table(n):
    """Use a FOR loop. Return a list of strings for n x 1 up to n x 10.
    times_table(3) -> ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 10 = 30"]
    """
    pass


def ex5_factorial(n):
    """Use a FOR loop. Return n! (n * (n-1) * ... * 1). factorial(0) is 1.
    factorial(5) -> 120
    """
    pass


def ex6_fizzbuzz(n):
    """Use a FOR loop. Return a list for 1..n where:
        multiple of 3 and 5 -> "FizzBuzz"
        multiple of 3       -> "Fizz"
        multiple of 5       -> "Buzz"
        otherwise           -> the number as a string
    fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
    """
    pass


# =====================================================================
# LEVEL 2 — while loops
# =====================================================================

def ex7_countdown(n):
    """Use a WHILE loop. Return a list from n down to 0.
    countdown(3) -> [3, 2, 1, 0]
    """
    pass


def ex8_digit_sum(n):
    """Use a WHILE loop. Add up the digits of a positive int. No str().
    Hint: n % 10 gives the last digit, n // 10 removes it.
    digit_sum(1234) -> 10
    """
    pass


def ex9_count_digits(n):
    """Use a WHILE loop. Return how many digits n has. No str() or len().
    count_digits(0) -> 1,  count_digits(98765) -> 5
    """
    pass


def ex10_first_power_over(base, limit):
    """Use a WHILE loop. Keep multiplying 1 by base until it is > limit.
    Return that first value.
    first_power_over(2, 100) -> 128
    """
    pass


def ex11_collatz_steps(n):
    """Use a WHILE loop. Count steps to reach 1:
        if n is even -> n = n // 2
        if n is odd  -> n = 3 * n + 1
    collatz_steps(6) -> 8   (6,3,10,5,16,8,4,2,1)
    """
    pass


def ex12_reverse_number(n):
    """Use a WHILE loop. Reverse the digits of a positive int. No str().
    reverse_number(1234) -> 4321
    """
    pass


# =====================================================================
# LEVEL 3 — strings
# =====================================================================

def ex13_count_vowels(s):
    """Use a FOR loop. Count vowels (a e i o u), upper or lower case.
    count_vowels("Apples and Bananas") -> 6
    """
    pass


def ex14_reverse_string(s):
    """Use a loop. Return s reversed. No [::-1] and no reversed().
    reverse_string("hello") -> "olleh"
    """
    pass


def ex15_count_char(s, ch):
    """Use a FOR loop. Count how many times ch appears in s. No .count().
    count_char("banana", "a") -> 3
    """
    pass


def ex16_remove_spaces(s):
    """Use a FOR loop. Return s without any spaces. No .replace() or .split().
    remove_spaces("a b  c") -> "abc"
    """
    pass


def ex17_split_words(sentence):
    """Use a FOR loop. Split sentence into a list of words on spaces.
    Skip empty words (double spaces). No .split().
    (You started this one in test.py!)
    split_words("hi  there you") -> ["hi", "there", "you"]
    """
    pass


def ex18_is_palindrome(s):
    """Use a loop. True if s reads the same backwards, ignoring case and spaces.
    No [::-1] and no reversed().
    is_palindrome("Race car") -> True,  is_palindrome("hello") -> False
    """
    pass


def ex19_capitalize_words(s):
    """Use a FOR loop. Uppercase the first letter of every word.
    No .title() or .capitalize(). (.upper() on one letter is OK.)
    capitalize_words("hello big world") -> "Hello Big World"
    """
    pass


def ex20_compress(s):
    """Use a loop. Replace runs of the same letter with letter + count.
    compress("aaabbc") -> "a3b2c1",  compress("") -> ""
    """
    pass


def ex21_longest_word(sentence):
    """Use a loop. Return the longest word. If tie, return the first one.
    You MAY use .split() here. No max().
    longest_word("the quick brown fox") -> "quick"
    """
    pass


# =====================================================================
# LEVEL 4 — lists
# =====================================================================

def ex22_find_max(nums):
    """Use a FOR loop. Return the biggest number. No max() or sorted().
    find_max([3, 9, 2]) -> 9
    """
    pass


def ex23_average(nums):
    """Use a FOR loop. Return the average. Empty list -> 0. No sum().
    average([2, 4, 6]) -> 4.0
    """
    pass


def ex24_only_positives(nums):
    """Use a FOR loop. Return a new list with only numbers > 0.
    only_positives([-1, 3, 0, 5]) -> [3, 5]
    """
    pass


def ex25_index_of(items, target):
    """Use a WHILE loop. Return the index of target, or -1 if missing.
    No .index() or .find().
    index_of(["a", "b", "c"], "c") -> 2
    """
    pass


def ex26_reverse_list(items):
    """Use a loop. Return a NEW reversed list. No [::-1], reversed(), .reverse().
    reverse_list([1, 2, 3]) -> [3, 2, 1]
    """
    pass


def ex27_remove_duplicates(items):
    """Use a FOR loop. Remove duplicates, keep the original order. No set().
    remove_duplicates([1, 2, 1, 3, 2]) -> [1, 2, 3]
    """
    pass


def ex28_running_total(nums):
    """Use a FOR loop. Each spot = sum of everything up to and including it.
    running_total([1, 2, 3, 4]) -> [1, 3, 6, 10]
    """
    pass


def ex29_second_largest(nums):
    """Use a FOR loop. Return the 2nd biggest DIFFERENT number.
    If there isn't one, return None. No max(), sorted(), .sort().
    second_largest([5, 1, 5, 3]) -> 3
    """
    pass


# =====================================================================
# LEVEL 5 — nested loops + putting it all together
# =====================================================================

def ex30_triangle(n):
    """Use NESTED FOR loops. Build a list of rows of stars. No "*" * n.
    triangle(3) -> ["*", "**", "***"]
    """
    pass


def ex31_is_prime(n):
    """Use a loop. True if n is prime (only divisible by 1 and itself).
    Numbers below 2 are not prime.
    is_prime(7) -> True,  is_prime(9) -> False
    """
    pass


def ex32_primes_up_to(n):
    """Use a loop AND call your ex31_is_prime function.
    primes_up_to(10) -> [2, 3, 5, 7]
    """
    pass


def ex33_pairs_that_sum(nums, target):
    """Use NESTED FOR loops. Return list of (a, b) pairs where a + b == target.
    Each pair uses two different positions; a comes before b in the list.
    pairs_that_sum([1, 2, 3, 4], 5) -> [(1, 4), (2, 3)]
    """
    pass


def ex34_flatten(list_of_lists):
    """Use NESTED FOR loops. Turn a list of lists into one list.
    flatten([[1, 2], [3], [], [4, 5]]) -> [1, 2, 3, 4, 5]
    """
    pass
