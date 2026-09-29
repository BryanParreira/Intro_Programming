"""
FOR + WHILE LOOP WORKOUT

HOW TO USE
    1. Pick an exercise. Replace `pass` (or `None`) with your answer.
    2. Run this file to check yourself:
           python3 for_while_practice.py        -> check everything
           python3 for_while_practice.py B      -> check only Part B
           python3 for_while_practice.py C5     -> check only exercise C5
    3. Go in order. Each part builds on the one before it.

PARTS
    A. Trace it     — read the loop, predict the result BY HAND (no running it!)
    B. for loops    — range(), stepping, looping over strings and lists
    C. while loops  — loop until a condition changes
    D. Both ways    — solve the same problem with for AND with while
    E. break + continue
    F. Nested loops — a loop inside a loop

RULES
    - Each exercise says which loop to use. The checker enforces it.
    - Some shortcuts are banned (sum(), .count(), **, "#" * n, ...).
      The point is to build them yourself with loops.
    - Always RETURN the answer. Don't just print it.

THE TWO LOOPS IN ONE SENTENCE
    for   -> "do this for EACH thing"         (you know how many times)
    while -> "keep doing this UNTIL it stops" (you don't know how many times)
"""


# =====================================================================
# PART A — TRACE IT
# Read each loop. Work it out on paper, step by step.
# Write the final value in the answer variable. Don't run the code!
# =====================================================================

# A1
#   total = 0
#   for i in range(1, 6, 2):
#       total += i
# What is total at the end?
A1 = 3

# A2
#   x = 10
#   count = 0
#   while x > 1:
#       x = x // 2
#       count += 1
# What is count at the end?
A2 = 3

# A3
#   result = ""
#   for ch in "loop":
#       result = ch + result
# What is result at the end? (it's a string)
A3 = None

# A4
#   nums = []
#   for i in range(5, 0, -2):
#       nums.append(i)
# What is nums at the end? (it's a list)
A4 = None

# A5
#   n = 0
#   while n < 20:
#       n += 7
# What is n at the end?
A5 = None

# A6
#   count = 0
#   for i in range(3):
#       for j in range(4):
#           count += 1
# What is count at the end?
A6 = None

# A7
#   for i in range(10):
#       if i * i > 20:
#           break
# What is i at the end?
A7 = None

# A8
#   total = 0
#   for i in range(8):
#       if i % 3 == 0:
#           continue
#       total += i
# What is total at the end?
A8 = None


# =====================================================================
# PART B — FOR LOOPS
# =====================================================================

def b1_count_by(start, stop, step):
    """Use a FOR loop with range(start, ?, step).
    Return every number from start to stop (inclusive), jumping by step.
    count_by(0, 20, 5) -> [0, 5, 10, 15, 20]
    """
    pass


def b2_backwards(n):
    """Use a FOR loop with a NEGATIVE step in range().
    Return a list from n down to 1.  No reversed(), .reverse(), or slicing.
    backwards(4) -> [4, 3, 2, 1]
    """
    pass


def b3_sum_of_odds(n):
    """Use a FOR loop. Add up all odd numbers from 1 to n. No sum().
    sum_of_odds(7) -> 16   (1 + 3 + 5 + 7)
    """
    pass


def b4_multiply_all(nums):
    """Use a FOR loop. Multiply every number in the list together.
    Empty list -> 1.
    multiply_all([2, 3, 4]) -> 24
    """
    pass


def b5_count_greater(nums, x):
    """Use a FOR loop. How many numbers in nums are bigger than x?
    count_greater([1, 8, 3, 9], 4) -> 2
    """
    pass


def b6_letter_positions(word, letter):
    """Use a FOR loop over range(len(word)).
    Return the list of indexes where letter appears. No .find() or .index().
    letter_positions("banana", "a") -> [1, 3, 5]
    """
    pass


def b7_every_other(items):
    """Use a FOR loop. Return items at index 0, 2, 4, ...  No slicing.
    every_other(["a", "b", "c", "d", "e"]) -> ["a", "c", "e"]
    """
    pass


def b8_squares(n):
    """Use a FOR loop. Return [1*1, 2*2, ..., n*n].  No **.
    squares(4) -> [1, 4, 9, 16]
    """
    pass


def b9_power(base, exp):
    """Use a FOR loop. Return base to the power of exp.  No ** or pow().
    power(2, 10) -> 1024,  power(5, 0) -> 1
    """
    pass


def b10_count_uppercase(s):
    """Use a FOR loop. Count the uppercase letters.
    Hint: "A".isupper() is True.
    count_uppercase("Hello World") -> 2
    """
    pass


# =====================================================================
# PART C — WHILE LOOPS
# Every while loop needs 3 things:
#   1. a starting value      2. a condition      3. something that CHANGES
# Forget #3 and you get an infinite loop.
# =====================================================================

def c1_halve_until_one(n):
    """Use a WHILE loop. Keep doing n = n // 2 until n is 1.
    Return every value you saw, including the start and the 1.
    halve_until_one(20) -> [20, 10, 5, 2, 1]
    """
    pass


def c2_double_until(start, limit):
    """Use a WHILE loop. Start at start, keep doubling while it's <= limit.
    Return every value that was <= limit.
    double_until(3, 50) -> [3, 6, 12, 24, 48]
    """
    pass


def c3_years_to_double(money, rate_percent):
    """Use a WHILE loop. Each year money grows by rate_percent.
    (money = money * (1 + rate_percent / 100))
    How many years until money is at least double what you started with?
    years_to_double(100, 10) -> 8
    """
    pass


def c4_count_until_over(nums, limit):
    """Use a WHILE loop with an index.
    Add numbers from the start of the list. Return how many you added when
    the total first goes OVER limit. If it never does, return -1.
    count_until_over([5, 5, 5, 5], 12) -> 3   (5, 10, 15 <- over!)
    """
    pass


def c5_gcd(a, b):
    """Use a WHILE loop. Greatest common divisor, using Euclid's trick:
        while b is not 0:  a becomes b,  b becomes a % b   (at the same time)
        then a is the answer.
    No math.gcd().
    gcd(48, 18) -> 6
    """
    pass


def c6_first_multiple(n, start):
    """Use a WHILE loop. Find the smallest number >= start that divides by n.
    first_multiple(7, 20) -> 21
    """
    pass


def c7_digits_list(n):
    """Use a WHILE loop. Return the digits of n as a list, in order. No str().
    Hint: n % 10 is the last digit, n // 10 chops it off.
          Put each digit at the FRONT of the list: lst.insert(0, digit)
    digits_list(472) -> [4, 7, 2],  digits_list(0) -> [0]
    """
    pass


def c8_count_down_by(start, step):
    """Use a WHILE loop. Count down from start by step, while above 0.
    count_down_by(10, 3) -> [10, 7, 4, 1]
    """
    pass


# =====================================================================
# PART D — BOTH WAYS
# Solve each problem twice: once with ONLY a for loop,
# once with ONLY a while loop. Any for loop can be a while loop!
#
#   for i in range(a, b):        i = a
#       ...              ==>     while i < b:
#                                    ...
#                                    i += 1
# =====================================================================

def d1_sum_evens_for(n):
    """FOR loop only. Add up even numbers from 1 to n. No sum().
    sum_evens(10) -> 30
    """
    pass


def d1_sum_evens_while(n):
    """WHILE loop only. Same as above."""
    pass


def d2_count_letter_for(s, ch):
    """FOR loop only. Count how many times ch appears in s. No .count().
    count_letter("mississippi", "s") -> 4
    """
    pass


def d2_count_letter_while(s, ch):
    """WHILE loop only. Same as above. Hint: use an index and s[index]."""
    pass


def d3_join_dashes_for(words):
    """FOR loop only. Join words with "-" between them. No .join().
    join_dashes(["a", "b", "c"]) -> "a-b-c",  join_dashes([]) -> ""
    """
    pass


def d3_join_dashes_while(words):
    """WHILE loop only. Same as above."""
    pass


# =====================================================================
# PART E — BREAK + CONTINUE
#   break    -> leave the loop RIGHT NOW
#   continue -> skip the rest of this turn, go to the next one
# =====================================================================

def e1_first_negative(nums):
    """Use a loop with BREAK. Return the first negative number, or None.
    (Save it in a variable, break, then return after the loop.)
    first_negative([3, -1, -5]) -> -1
    """
    pass


def e2_sum_skip_threes(n):
    """Use a loop with CONTINUE. Add 1..n but skip multiples of 3.
    sum_skip_threes(10) -> 37   (1+2+4+5+7+8+10)
    """
    pass


def e3_sum_until_zero(nums):
    """Use a loop with BREAK. Add numbers until you hit a 0, then stop.
    sum_until_zero([4, 5, 0, 100]) -> 9
    """
    pass


def e4_without_vowels(s):
    """Use a loop with CONTINUE. Return s with all vowels removed (any case).
    without_vowels("Education rocks") -> "dctn rcks"
    """
    pass


def e5_tries_needed(attempts, password):
    """Use a WHILE loop with BREAK.
    attempts is a list of guesses, in order. Return which try was correct
    (1 = first try). If none are correct, return -1.
    tries_needed(["123", "abc", "secret"], "secret") -> 3
    """
    pass


# =====================================================================
# PART F — NESTED LOOPS
# The inner loop runs ALL the way through for EACH turn of the outer loop.
# =====================================================================

def f1_times_grid(n):
    """NESTED for loops. Return an n x n list of lists: row i, col j = i * j
    (start counting at 1).
    times_grid(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    pass


def f2_rectangle(width, height):
    """NESTED for loops. Return a list of rows made of "#".  No "#" * width.
    rectangle(4, 2) -> ["####", "####"]
    """
    pass


def f3_number_triangle(n):
    """NESTED for loops.
    number_triangle(4) -> ["1", "12", "123", "1234"]
    """
    pass


def f4_upside_down(n):
    """NESTED for loops. No "*" * n.
    upside_down(3) -> ["***", "**", "*"]
    """
    pass


def f5_count_common(a, b):
    """NESTED for loops. How many items in a also appear in b?
    Don't use the `in` operator to check (for x in a is fine).
    count_common([1, 2, 3, 4], [2, 4, 6]) -> 2
    """
    pass


def f6_has_duplicate(items):
    """NESTED for loops. True if any item appears twice. No set(), .count(), `in`.
    Hint: compare index i with every index j after it.
    has_duplicate([1, 2, 3, 2]) -> True
    """
    pass


# =====================================================================
# =====================================================================
#            CHECKER BELOW — no need to edit anything down here
# =====================================================================
# =====================================================================

import ast
import copy
import hashlib
import inspect
import signal
import sys
import textwrap

GREEN, RED, GREY, BOLD, RESET = "\033[92m", "\033[91m", "\033[90m", "\033[1m", "\033[0m"

# Answers are hashed so you can't peek. Work them out!
TRACE_ANSWERS = {
    "A1": "19581e27de7c", "A2": "4e07408562be", "A3": "4675e9aaa74f",
    "A4": "32b8dea50d5c", "A5": "6f4b6612125f", "A6": "6b51d431df5d",
    "A7": "ef2d127de37b", "A8": "9400f1b21cb5",
}

# id: (function name, loop rule, banned, required keywords, tests)
#   loop rule: "for", "while", "for_only", "while_only", "nested", "any"
#   banned: call names, or "slice", "step_slice", "**", "str*", "in"
#   required: "break", "continue"
EXERCISES = {
    "B1": ("b1_count_by", "for", [], [], [
        ((0, 20, 5), [0, 5, 10, 15, 20]), ((1, 10, 3), [1, 4, 7, 10]),
        ((2, 9, 4), [2, 6])]),
    "B2": ("b2_backwards", "for", ["reversed", "reverse", "step_slice"], [], [
        ((4,), [4, 3, 2, 1]), ((1,), [1]), ((0,), [])]),
    "B3": ("b3_sum_of_odds", "for", ["sum"], [], [
        ((7,), 16), ((1,), 1), ((10,), 25), ((0,), 0)]),
    "B4": ("b4_multiply_all", "for", [], [], [
        (([2, 3, 4],), 24), (([],), 1), (([5, 0, 3],), 0)]),
    "B5": ("b5_count_greater", "for", [], [], [
        (([1, 8, 3, 9], 4), 2), (([], 0), 0), (([5, 5], 5), 0)]),
    "B6": ("b6_letter_positions", "for", ["find", "index"], [], [
        (("banana", "a"), [1, 3, 5]), (("hello", "z"), []), (("aa", "a"), [0, 1])]),
    "B7": ("b7_every_other", "for", ["slice"], [], [
        ((["a", "b", "c", "d", "e"],), ["a", "c", "e"]), (([1, 2],), [1]), (([],), [])]),
    "B8": ("b8_squares", "for", ["**", "pow"], [], [
        ((4,), [1, 4, 9, 16]), ((1,), [1]), ((0,), [])]),
    "B9": ("b9_power", "for", ["**", "pow"], [], [
        ((2, 10), 1024), ((5, 0), 1), ((3, 3), 27), ((7, 1), 7)]),
    "B10": ("b10_count_uppercase", "for", [], [], [
        (("Hello World",), 2), (("abc",), 0), (("ABC def G",), 4)]),

    "C1": ("c1_halve_until_one", "while", [], [], [
        ((20,), [20, 10, 5, 2, 1]), ((1,), [1]), ((8,), [8, 4, 2, 1])]),
    "C2": ("c2_double_until", "while", [], [], [
        ((3, 50), [3, 6, 12, 24, 48]), ((5, 4), []), ((1, 8), [1, 2, 4, 8])]),
    "C3": ("c3_years_to_double", "while", [], [], [
        ((100, 10), 8), ((100, 7), 11), ((100, 100), 1), ((50, 25), 4)]),
    "C4": ("c4_count_until_over", "while", [], [], [
        (([5, 5, 5, 5], 12), 3), (([1, 2], 100), -1), (([50], 10), 1), (([], 0), -1)]),
    "C5": ("c5_gcd", "while", ["gcd"], [], [
        ((48, 18), 6), ((7, 5), 1), ((10, 10), 10), ((100, 75), 25)]),
    "C6": ("c6_first_multiple", "while", [], [], [
        ((7, 20), 21), ((5, 10), 10), ((3, 1), 3)]),
    "C7": ("c7_digits_list", "while", ["str"], [], [
        ((472,), [4, 7, 2]), ((0,), [0]), ((1005,), [1, 0, 0, 5]), ((9,), [9])]),
    "C8": ("c8_count_down_by", "while", [], [], [
        ((10, 3), [10, 7, 4, 1]), ((5, 5), [5]), ((0, 2), [])]),

    "D1a": ("d1_sum_evens_for", "for_only", ["sum"], [], [
        ((10,), 30), ((1,), 0), ((7,), 12)]),
    "D1b": ("d1_sum_evens_while", "while_only", ["sum"], [], [
        ((10,), 30), ((1,), 0), ((7,), 12)]),
    "D2a": ("d2_count_letter_for", "for_only", ["count"], [], [
        (("mississippi", "s"), 4), (("", "a"), 0), (("aaa", "b"), 0)]),
    "D2b": ("d2_count_letter_while", "while_only", ["count"], [], [
        (("mississippi", "s"), 4), (("", "a"), 0), (("aaa", "b"), 0)]),
    "D3a": ("d3_join_dashes_for", "for_only", ["join"], [], [
        ((["a", "b", "c"],), "a-b-c"), (([],), ""), ((["solo"],), "solo")]),
    "D3b": ("d3_join_dashes_while", "while_only", ["join"], [], [
        ((["a", "b", "c"],), "a-b-c"), (([],), ""), ((["solo"],), "solo")]),

    "E1": ("e1_first_negative", "any", [], ["break"], [
        (([3, -1, -5],), -1), (([1, 2],), None), (([-7],), -7), (([],), None)]),
    "E2": ("e2_sum_skip_threes", "any", ["sum"], ["continue"], [
        ((10,), 37), ((2,), 3), ((3,), 3), ((0,), 0)]),
    "E3": ("e3_sum_until_zero", "any", ["sum"], ["break"], [
        (([4, 5, 0, 100],), 9), (([1, 2],), 3), (([0, 5],), 0), (([],), 0)]),
    "E4": ("e4_without_vowels", "any", ["replace"], ["continue"], [
        (("Education rocks",), "dctn rcks"), (("xyz",), "xyz"), (("AEIOU",), "")]),
    "E5": ("e5_tries_needed", "while", ["index"], ["break"], [
        ((["123", "abc", "secret"], "secret"), 3), ((["secret"], "secret"), 1),
        ((["a", "b"], "secret"), -1), (([], "x"), -1)]),

    "F1": ("f1_times_grid", "nested", [], [], [
        ((3,), [[1, 2, 3], [2, 4, 6], [3, 6, 9]]), ((1,), [[1]]), ((0,), [])]),
    "F2": ("f2_rectangle", "nested", ["str*"], [], [
        ((4, 2), ["####", "####"]), ((1, 3), ["#", "#", "#"]), ((3, 0), [])]),
    "F3": ("f3_number_triangle", "nested", [], [], [
        ((4,), ["1", "12", "123", "1234"]), ((1,), ["1"]), ((0,), [])]),
    "F4": ("f4_upside_down", "nested", ["str*"], [], [
        ((3,), ["***", "**", "*"]), ((1,), ["*"]), ((0,), [])]),
    "F5": ("f5_count_common", "nested", ["in"], [], [
        (([1, 2, 3, 4], [2, 4, 6]), 2), (([], [1]), 0), ((["a", "b"], ["c"]), 0),
        ((["x", "y"], ["y", "x"]), 2)]),
    "F6": ("f6_has_duplicate", "nested", ["set", "count", "in"], [], [
        (([1, 2, 3, 2],), True), (([1, 2, 3],), False), (([],), False),
        ((["a", "a"],), True)]),
}

PART_NAMES = {
    "A": "PART A — trace it", "B": "PART B — for loops", "C": "PART C — while loops",
    "D": "PART D — both ways", "E": "PART E — break + continue",
    "F": "PART F — nested loops",
}


def _tree(func):
    return ast.parse(textwrap.dedent(inspect.getsource(func))).body[0]


def _not_started(fn):
    body = fn.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    return all(isinstance(stmt, ast.Pass) for stmt in body)


def _has_nested_for(fn):
    for outer in ast.walk(fn):
        if isinstance(outer, ast.For):
            if any(n is not outer and isinstance(n, ast.For) for n in ast.walk(outer)):
                return True
    return False


def _rule_problems(fn, loop, banned, required):
    nodes = list(ast.walk(fn))
    has_for = any(isinstance(n, (ast.For, ast.comprehension)) for n in nodes)
    has_while = any(isinstance(n, ast.While) for n in nodes)
    calls = set()
    for n in nodes:
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Name):
                calls.add(n.func.id)
            elif isinstance(n.func, ast.Attribute):
                calls.add(n.func.attr)

    problems = []
    if loop in ("for", "for_only") and not has_for:
        problems.append("use a FOR loop")
    if loop in ("while", "while_only") and not has_while:
        problems.append("use a WHILE loop")
    if loop == "for_only" and has_while:
        problems.append("no while loop in this one — for only")
    if loop == "while_only" and has_for:
        problems.append("no for loop in this one — while only")
    if loop == "nested" and not _has_nested_for(fn):
        problems.append("use NESTED for loops (a for inside a for)")
    if loop == "any" and not (has_for or has_while):
        problems.append("use a loop")

    for item in banned:
        if item == "slice":
            if any(isinstance(n, ast.Slice) for n in nodes):
                problems.append("no slicing like [::2] — use the loop")
        elif item == "step_slice":
            if any(isinstance(n, ast.Slice) and n.step is not None for n in nodes):
                problems.append("no [::-1] — use the loop")
        elif item == "**":
            if any(isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow) for n in nodes):
                problems.append("no ** — multiply in a loop")
        elif item == "str*":
            for n in nodes:
                if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
                    if any(isinstance(s, ast.Constant) and isinstance(s.value, str)
                           for s in (n.left, n.right)):
                        problems.append('no "#" * n — build it with the inner loop')
                        break
        elif item == "in":
            if any(isinstance(n, ast.Compare) and any(isinstance(op, (ast.In, ast.NotIn))
                                                       for op in n.ops) for n in nodes):
                problems.append("no `x in list` check — compare with a second loop")
        elif item in calls:
            problems.append(f"don't use {item}()")

    if "break" in required and not any(isinstance(n, ast.Break) for n in nodes):
        problems.append("use break")
    if "continue" in required and not any(isinstance(n, ast.Continue) for n in nodes):
        problems.append("use continue")
    return problems


class _TooSlow(Exception):
    pass


def _alarm(signum, frame):
    raise _TooSlow()


def _check_trace(key):
    answer = globals()[key]
    if answer is None:
        print(f"{GREY}  ·  {key}  (not answered){RESET}")
        return False
    digest = hashlib.sha256(repr(answer).encode()).hexdigest()[:12]
    if digest == TRACE_ANSWERS[key]:
        print(f"{GREEN}  ✓  {key}{RESET}")
        return True
    print(f"{RED}  ✗  {key}  — {answer!r} is not it. Trace it again, one turn at a time.{RESET}")
    print("       Tip: make a little table with a column for each variable.")
    return False


def _check_exercise(key):
    name, loop, banned, required, tests = EXERCISES[key]
    func = globals()[name]
    fn = _tree(func)
    label = f"{key:<4} {name.split('_', 1)[1]}"
    short = name.split("_", 1)[1]

    if _not_started(fn):
        print(f"{GREY}  ·  {label}  (not started){RESET}")
        return False

    for args, expected in tests:
        call = f"{short}({', '.join(repr(a) for a in args)})"
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(2)
        try:
            got = func(*copy.deepcopy(args))
        except _TooSlow:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {call} ran over 2 seconds — infinite loop?")
            print("       Check: does something in your while condition change every turn?")
            return False
        except Exception as err:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {call} crashed: {type(err).__name__}: {err}")
            return False
        finally:
            signal.alarm(0)
        if got != expected:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {call}")
            print(f"       expected: {expected!r}")
            print(f"       got:      {got!r}")
            if got is None:
                print("       (got None — did you forget to return?)")
            return False

    problems = _rule_problems(fn, loop, banned, required)
    if problems:
        print(f"{RED}  ✗  {label}  — right answers, but: {'; '.join(problems)}{RESET}")
        return False

    print(f"{GREEN}  ✓  {label}{RESET}")
    return True


def _run_checker():
    all_keys = list(TRACE_ANSWERS) + list(EXERCISES)
    wanted = [a.upper() for a in sys.argv[1:]]
    picked = [k for k in all_keys
              if not wanted or k.upper() in wanted or k[0] in wanted]
    if not picked:
        print(f"Nothing matches {' '.join(sys.argv[1:])}. Try: A, B, C3, D1a ...")
        return

    passed = 0
    part = None
    for key in picked:
        if key[0] != part and len(picked) > 1:
            part = key[0]
            print(f"\n{BOLD}{PART_NAMES[part]}{RESET}")
        passed += _check_trace(key) if key in TRACE_ANSWERS else _check_exercise(key)

    print(f"\n{BOLD}{passed}/{len(picked)} passed{RESET}")
    if passed == len(all_keys):
        print("Every loop mastered. Nice work!")


if __name__ == "__main__":
    _run_checker()

