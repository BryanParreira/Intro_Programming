"""
Checker for practice.py

    python3 check.py        -> check every exercise
    python3 check.py 7      -> check only exercise 7
    python3 check.py 3 8 12 -> check exercises 3, 8 and 12
"""

import ast
import copy
import inspect
import signal
import sys
import textwrap

if "--solutions" in sys.argv:
    sys.argv.remove("--solutions")
    import solutions as practice
else:
    import practice


GREEN = "\033[92m"
RED = "\033[91m"
GREY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

NO_REVERSE_SLICE = "[::-1]"
NO_STAR_TIMES_STR = '"*" * n'

# number: (function name, loop required, banned things, tests)
# loop required: "for", "while", "any", "nested"
# tests: list of (args, expected)
EXERCISES = {
    1: ("ex1_count_up", "for", [], [
        ((5,), [1, 2, 3, 4, 5]), ((1,), [1]), ((0,), [])]),
    2: ("ex2_sum_to", "for", ["sum"], [
        ((4,), 10), ((1,), 1), ((100,), 5050), ((0,), 0)]),
    3: ("ex3_evens_between", "for", [], [
        ((5, 12), [6, 8, 10, 12]), ((2, 6), [2, 4, 6]), ((7, 7), [])]),
    4: ("ex4_times_table", "for", [], [
        ((3,), [f"3 x {i} = {3 * i}" for i in range(1, 11)]),
        ((7,), [f"7 x {i} = {7 * i}" for i in range(1, 11)])]),
    5: ("ex5_factorial", "for", [], [
        ((5,), 120), ((0,), 1), ((1,), 1), ((10,), 3628800)]),
    6: ("ex6_fizzbuzz", "for", [], [
        ((5,), ["1", "2", "Fizz", "4", "Buzz"]),
        ((15,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
                 "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])]),

    7: ("ex7_countdown", "while", [], [
        ((3,), [3, 2, 1, 0]), ((0,), [0])]),
    8: ("ex8_digit_sum", "while", ["str"], [
        ((1234,), 10), ((5,), 5), ((9999,), 36), ((1000,), 1)]),
    9: ("ex9_count_digits", "while", ["str", "len"], [
        ((0,), 1), ((7,), 1), ((98765,), 5), ((100,), 3)]),
    10: ("ex10_first_power_over", "while", [], [
        ((2, 100), 128), ((3, 10), 27), ((10, 999), 1000), ((2, 0), 1)]),
    11: ("ex11_collatz_steps", "while", [], [
        ((6,), 8), ((1,), 0), ((27,), 111)]),
    12: ("ex12_reverse_number", "while", ["str"], [
        ((1234,), 4321), ((5,), 5), ((120,), 21)]),

    13: ("ex13_count_vowels", "for", [], [
        (("Apples and Bananas",), 6), (("xyz",), 0), (("AEIOU",), 5)]),
    14: ("ex14_reverse_string", "any", ["reversed", NO_REVERSE_SLICE], [
        (("hello",), "olleh"), (("",), ""), (("ab c",), "c ba")]),
    15: ("ex15_count_char", "for", ["count"], [
        (("banana", "a"), 3), (("banana", "z"), 0), (("aaa", "a"), 3)]),
    16: ("ex16_remove_spaces", "for", ["replace", "split"], [
        (("a b  c",), "abc"), (("nospace",), "nospace"), (("   ",), "")]),
    17: ("ex17_split_words", "for", ["split"], [
        (("hi  there you",), ["hi", "there", "you"]),
        (("one",), ["one"]), ((" lead and trail ",), ["lead", "and", "trail"]),
        (("",), [])]),
    18: ("ex18_is_palindrome", "any", ["reversed", NO_REVERSE_SLICE], [
        (("Race car",), True), (("hello",), False), (("a",), True),
        (("Never odd or even",), True)]),
    19: ("ex19_capitalize_words", "for", ["title", "capitalize"], [
        (("hello big world",), "Hello Big World"), (("a",), "A"),
        (("already Upper",), "Already Upper")]),
    20: ("ex20_compress", "any", [], [
        (("aaabbc",), "a3b2c1"), (("",), ""), (("a",), "a1"),
        (("aabaa",), "a2b1a2")]),
    21: ("ex21_longest_word", "any", ["max"], [
        (("the quick brown fox",), "quick"), (("hi",), "hi"),
        (("cat dog",), "cat")]),

    22: ("ex22_find_max", "for", ["max", "sorted", "sort"], [
        (([3, 9, 2],), 9), (([-5, -2, -9],), -2), (([7],), 7)]),
    23: ("ex23_average", "for", ["sum"], [
        (([2, 4, 6],), 4.0), (([1, 2],), 1.5), (([],), 0)]),
    24: ("ex24_only_positives", "for", [], [
        (([-1, 3, 0, 5],), [3, 5]), (([-1, -2],), []), (([],), [])]),
    25: ("ex25_index_of", "while", ["index", "find"], [
        ((["a", "b", "c"], "c"), 2), ((["a", "b"], "z"), -1),
        (([], "a"), -1), (([4, 4], 4), 0)]),
    26: ("ex26_reverse_list", "any", ["reversed", "reverse", NO_REVERSE_SLICE], [
        (([1, 2, 3],), [3, 2, 1]), (([],), []), ((["x"],), ["x"])]),
    27: ("ex27_remove_duplicates", "for", ["set", "fromkeys"], [
        (([1, 2, 1, 3, 2],), [1, 2, 3]), (([],), []),
        ((["b", "a", "b"],), ["b", "a"])]),
    28: ("ex28_running_total", "for", ["sum"], [
        (([1, 2, 3, 4],), [1, 3, 6, 10]), (([],), []), (([5, -5],), [5, 0])]),
    29: ("ex29_second_largest", "for", ["max", "sorted", "sort"], [
        (([5, 1, 5, 3],), 3), (([4, 4],), None), (([1],), None),
        (([-1, -3, -2],), -2)]),

    30: ("ex30_triangle", "nested", [NO_STAR_TIMES_STR], [
        ((3,), ["*", "**", "***"]), ((1,), ["*"]), ((0,), [])]),
    31: ("ex31_is_prime", "any", [], [
        ((7,), True), ((9,), False), ((2,), True), ((1,), False),
        ((0,), False), ((97,), True), ((91,), False)]),
    32: ("ex32_primes_up_to", "any", [], [
        ((10,), [2, 3, 5, 7]), ((1,), []), ((20,), [2, 3, 5, 7, 11, 13, 17, 19])]),
    33: ("ex33_pairs_that_sum", "nested", [], [
        (([1, 2, 3, 4], 5), [(1, 4), (2, 3)]), (([1, 1], 2), [(1, 1)]),
        (([1, 2], 10), [])]),
    34: ("ex34_flatten", "nested", [], [
        (([[1, 2], [3], [], [4, 5]],), [1, 2, 3, 4, 5]), (([],), [])]),
}

MUST_CALL = {32: "ex31_is_prime"}


# ---------------------------------------------------------------------
# Code inspection
# ---------------------------------------------------------------------

def get_tree(func):
    source = textwrap.dedent(inspect.getsource(func))
    return ast.parse(source).body[0]


def not_started(fn_node):
    body = fn_node.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    return all(isinstance(stmt, ast.Pass) for stmt in body)


def is_for(node):
    return isinstance(node, (ast.For, ast.comprehension))


def has_nested_for(fn_node):
    for outer in ast.walk(fn_node):
        if isinstance(outer, ast.For):
            for inner in ast.walk(outer):
                if inner is not outer and isinstance(inner, ast.For):
                    return True
    return False


def called_names(fn_node):
    names = set()
    for node in ast.walk(fn_node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                names.add(node.func.attr)
    return names


def uses_step_slice(fn_node):
    for node in ast.walk(fn_node):
        if isinstance(node, ast.Slice) and node.step is not None:
            return True
    return False


def uses_string_times(fn_node):
    for node in ast.walk(fn_node):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            for side in (node.left, node.right):
                if isinstance(side, ast.Constant) and isinstance(side.value, str):
                    return True
    return False


def rule_problems(num, fn_node):
    _, loop, banned, _ = EXERCISES[num]
    problems = []
    nodes = list(ast.walk(fn_node))
    has_for = any(is_for(n) for n in nodes)
    has_while = any(isinstance(n, ast.While) for n in nodes)

    if loop == "for" and not has_for:
        problems.append("use a FOR loop")
    elif loop == "while" and not has_while:
        problems.append("use a WHILE loop")
    elif loop == "any" and not (has_for or has_while):
        problems.append("use a loop")
    elif loop == "nested" and not has_nested_for(fn_node):
        problems.append("use NESTED for loops (a for loop inside a for loop)")

    calls = called_names(fn_node)
    for item in banned:
        if item == NO_REVERSE_SLICE:
            if uses_step_slice(fn_node):
                problems.append("no [::-1] slicing — build it with a loop")
        elif item == NO_STAR_TIMES_STR:
            if uses_string_times(fn_node):
                problems.append('no "*" * n — build each row with a loop')
        elif item in calls:
            problems.append(f"don't use {item}()")

    if num in MUST_CALL and MUST_CALL[num] not in calls:
        problems.append(f"call your {MUST_CALL[num]}() function")
    return problems


# ---------------------------------------------------------------------
# Running tests
# ---------------------------------------------------------------------

class TookTooLong(Exception):
    pass


def _alarm(signum, frame):
    raise TookTooLong()


def call_with_timeout(func, args, seconds=2):
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(seconds)
    try:
        return func(*args)
    finally:
        signal.alarm(0)


def show_call(name, args):
    short = name.split("_", 1)[1]
    return f"{short}({', '.join(repr(a) for a in args)})"


def check(num):
    name, _, _, tests = EXERCISES[num]
    func = getattr(practice, name)
    fn_node = get_tree(func)
    label = f"{num:>2}. {name.split('_', 1)[1]}"

    if not_started(fn_node):
        print(f"{GREY}  ·  {label}  (not started){RESET}")
        return False

    for args, expected in tests:
        try:
            got = call_with_timeout(func, copy.deepcopy(args))
        except TookTooLong:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {show_call(name, args)} ran over 2 seconds.")
            print("       Infinite loop? Check your while condition changes each time.")
            return False
        except Exception as err:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {show_call(name, args)} crashed: {type(err).__name__}: {err}")
            return False
        if got != expected:
            print(f"{RED}  ✗  {label}{RESET}")
            print(f"       {show_call(name, args)}")
            print(f"       expected: {expected!r}")
            print(f"       got:      {got!r}")
            if got is None:
                print("       (got None — did you forget to return?)")
            return False

    problems = rule_problems(num, fn_node)
    if problems:
        print(f"{RED}  ✗  {label}  — answers right, but: {'; '.join(problems)}{RESET}")
        return False

    print(f"{GREEN}  ✓  {label}{RESET}")
    return True


LEVELS = [
    (1, "LEVEL 1 — for loops + range()"),
    (7, "LEVEL 2 — while loops"),
    (13, "LEVEL 3 — strings"),
    (22, "LEVEL 4 — lists"),
    (30, "LEVEL 5 — nested loops + putting it together"),
]


def main():
    picked = [int(a) for a in sys.argv[1:]] or list(EXERCISES)
    level_starts = dict(LEVELS)
    passed = 0
    for num in picked:
        if num not in EXERCISES:
            print(f"No exercise {num}. Pick 1-{len(EXERCISES)}.")
            continue
        if len(picked) > 1 and num in level_starts:
            print(f"\n{BOLD}{level_starts[num]}{RESET}")
        passed += check(num)
    print(f"\n{BOLD}{passed}/{len(picked)} passed{RESET}")
    if passed == len(EXERCISES):
        print("All done. You are a loop master.")


if __name__ == "__main__":
    main()
