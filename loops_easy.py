"""
EASY LOOP PRACTICE

HOW TO USE
    1. Read the EXAMPLE. It is already solved — study how it works.
    2. Do the YOUR TURN exercises under it. Delete `pass` and write your code.
    3. Run:   python3 loops_easy.py
       It checks your exercises in order and tells you what to fix next.

Each exercise only needs 3–5 lines. The skeleton in the comments shows the
shape — copy it and fill in the ___ parts.
"""


# =====================================================================
# STEP 1 — for + range()
#
#   range(1, 6)      -> 1, 2, 3, 4, 5        (stops BEFORE the 2nd number)
#   range(0, 10, 2)  -> 0, 2, 4, 6, 8        (3rd number = jump size)
#   range(5, 0, -1)  -> 5, 4, 3, 2, 1        (negative jump = count down)
# =====================================================================

# EXAMPLE (already solved)
import textwrap
import signal
import inspect
import ast


def example_one_to_five():
    result = []
    for number in range(1, 6):
        result.append(number)
    return result
# example_one_to_five() gives [1, 2, 3, 4, 5]


# YOUR TURN
def ex1_one_to_ten():
    result = []
    for number in range(1, 11):
        result.append(number)
    return result
    """Return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

    result = []
    for number in range(___, ___):
        result.append(number)
    return result
    """
    pass


def ex2_zero_to_twenty_by_twos():
    result = []
    for number in range(0, 21):
        if number % 2 == 0:
            result.append(number)
    return result
    """Return [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
    Hint: range needs 3 numbers here.
    """
    pass


def ex3_ten_down_to_one():
    result = []
    for number in range(10, 0, -1):
        result.append(number)
    return result
    """Return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].
    Hint: look at range(5, 0, -1) above.
    """
    pass


def ex4_add_one_to_ten():
    """Return 1 + 2 + 3 + ... + 10 (the answer is one number).

    total = 0
    for number in range(___, ___):
        total = total + number
    return total
    """
    pass


# =====================================================================
# STEP 2 — for over a STRING
#   for letter in "cat":   -> letter is "c", then "a", then "t"
# =====================================================================

# EXAMPLE (already solved)
def example_letters(word):
    result = []
    for letter in word:
        result.append(letter)
    return result
# example_letters("cat") gives ["c", "a", "t"]


# YOUR TURN
def ex5_count_letters(word):
    """Count the letters in word using a loop. Don't use len().
    count_letters("hello") -> 5

    count = 0
    for letter in word:
        count = ___
    return count
    """
    pass


def ex6_count_a(word):
    """Count how many "a" letters are in word.
    count_a("banana") -> 3

    Same as ex5, but only count when:   if letter == "a":
    """
    pass


def ex7_double_letters(word):
    """Write every letter twice.
    double_letters("hi") -> "hhii"

    result = ""
    for letter in word:
        result = result + ___
    return result
    """
    pass


# =====================================================================
# STEP 3 — for over a LIST
#   for item in [4, 7, 9]:   -> item is 4, then 7, then 9
# =====================================================================

# EXAMPLE (already solved)
def example_total(nums):
    total = 0
    for num in nums:
        total = total + num
    return total
# example_total([1, 2, 3]) gives 6


# YOUR TURN
def ex8_count_items(items):
    """Count the items in the list with a loop. Don't use len().
    count_items(["a", "b", "c"]) -> 3
    """
    pass


def ex9_double_all(nums):
    """Return a NEW list with every number doubled.
    double_all([1, 2, 3]) -> [2, 4, 6]

    result = []
    for num in nums:
        result.append(___)
    return result
    """
    pass


def ex10_count_big(nums):
    """Count how many numbers are bigger than 10.
    count_big([5, 20, 11, 3]) -> 2
    """
    pass


def ex11_say_hello(names):
    """Put "Hello " in front of every name.
    say_hello(["Bryan", "Matt"]) -> ["Hello Bryan", "Hello Matt"]
    """
    pass


# =====================================================================
# STEP 4 — while loops
#   A while loop needs 3 things:
#     1. a start value         number = 1
#     2. a condition           while number <= 5:
#     3. a CHANGE each turn    number = number + 1
#   Forget #3 and the loop never stops!
# =====================================================================

# EXAMPLE (already solved)
def example_while_one_to_five():
    result = []
    number = 1
    while number <= 5:
        result.append(number)
        number = number + 1
    return result
# example_while_one_to_five() gives [1, 2, 3, 4, 5]


# YOUR TURN
def ex12_while_one_to_ten():
    """Use WHILE. Return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    Hint: copy the example and change one number.
    """
    pass


def ex13_while_countdown(n):
    """Use WHILE. Count down from n to 1.
    while_countdown(5) -> [5, 4, 3, 2, 1]

    result = []
    while n >= ___:
        result.append(n)
        n = ___
    return result
    """
    pass


def ex14_while_doubling():
    """Use WHILE. Start at 1 and keep doubling while the number is under 100.
    Return [1, 2, 4, 8, 16, 32, 64].
    Hint: the change each turn is   number = number * 2
    """
    pass


# =====================================================================
# STEP 5 — if INSIDE a loop
# =====================================================================

# EXAMPLE (already solved)
def example_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result
# example_evens([1, 2, 3, 4]) gives [2, 4]


# YOUR TURN
def ex15_odds(nums):
    """Keep only the odd numbers.
    odds([1, 2, 3, 4, 5]) -> [1, 3, 5]
    Hint: odd means   num % 2 == 1
    """
    pass


def ex16_short_names(names):
    """Keep only names with 5 letters or fewer. (len() is OK here.)
    short_names(["Bryan", "Landon", "Matt"]) -> ["Bryan", "Matt"]
    """
    pass


def ex17_starts_with_b(words):
    """Keep only words that start with "b".
    starts_with_b(["banana", "apple", "berry"]) -> ["banana", "berry"]
    Hint: word[0] is the first letter.
    """
    pass


# =====================================================================
#          CHECKER BELOW — you don't need to change anything here
# =====================================================================


GREEN, RED, GREY, BOLD, RESET = "\033[92m", "\033[91m", "\033[90m", "\033[1m", "\033[0m"

# (function, loop needed, banned function, tests, hint if wrong)
EXERCISES = [
    (ex1_one_to_ten, "for", None, [((), list(range(1, 11)))],
     "range stops BEFORE the 2nd number. To include 10, what should it be?"),
    (ex2_zero_to_twenty_by_twos, "for", None, [((), list(range(0, 21, 2)))],
     "range(start, stop, jump). Start 0, jump 2. Stop must be past 20."),
    (ex3_ten_down_to_one, "for", None, [((), list(range(10, 0, -1)))],
     "range(10, ___, -1). It stops BEFORE the 2nd number, so to reach 1 use 0."),
    (ex4_add_one_to_ten, "for", None, [((), 55)],
     "Start total at 0 BEFORE the loop. Inside the loop: total = total + number."),
    (ex5_count_letters, "for", "len", [(("hello",), 5), (("",), 0), (("a",), 1)],
     "Each time the loop runs, add 1 to count:  count = count + 1"),
    (ex6_count_a, "for", "count", [(("banana",), 3), (("xyz",), 0), (("a",), 1)],
     "Only add 1 when the letter is \"a\". Put the  count = count + 1  inside the if."),
    (ex7_double_letters, "for", None, [(("hi",), "hhii"), (("",), ""), (("abc",), "aabbcc")],
     "Add the letter twice each turn:  result = result + letter + letter"),
    (ex8_count_items, "for", "len", [((["a", "b", "c"],), 3), (([],), 0)],
     "Same idea as ex5 — start at 0, add 1 each turn."),
    (ex9_double_all, "for", None, [(([1, 2, 3],), [2, 4, 6]), (([],), []), (([5],), [10])],
     "Inside the loop:  result.append(num * 2)"),
    (ex10_count_big, "for", None, [(([5, 20, 11, 3],), 2), (([],), 0), (([10],), 0)],
     "Bigger than 10 means  num > 10  (10 itself does NOT count)."),
    (ex11_say_hello, "for", None,
     [((["Bryan", "Matt"],), ["Hello Bryan", "Hello Matt"]), (([],), [])],
     "Don't forget the space:  \"Hello \" + name"),
    (ex12_while_one_to_ten, "while", None, [((), list(range(1, 11)))],
     "Copy example_while_one_to_five and change the 5 to 10."),
    (ex13_while_countdown, "while", None, [((5,), [5, 4, 3, 2, 1]), ((1,), [1]), ((0,), [])],
     "Keep going while n >= 1. Each turn:  n = n - 1"),
    (ex14_while_doubling, "while", None, [((), [1, 2, 4, 8, 16, 32, 64])],
     "number = 1 to start. while number < 100: append it, then number = number * 2"),
    (ex15_odds, "for", None, [(([1, 2, 3, 4, 5],), [1, 3, 5]), (([2, 4],), [])],
     "Copy example_evens and change  == 0  to  == 1"),
    (ex16_short_names, "for", None,
     [((["Bryan", "Landon", "Matt"],), ["Bryan", "Matt"]), (([],), [])],
     "if len(name) <= 5:  then append it."),
    (ex17_starts_with_b, "for", None,
     [((["banana", "apple", "berry"],), ["banana", "berry"]), ((["kiwi"],), [])],
     "if word[0] == \"b\":  then append it."),
]


def _info(func):
    tree = ast.parse(textwrap.dedent(inspect.getsource(func))).body[0]
    body = tree.body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    not_started = all(isinstance(s, ast.Pass) for s in body)
    nodes = list(ast.walk(tree))
    has_for = any(isinstance(n, (ast.For, ast.comprehension)) for n in nodes)
    has_while = any(isinstance(n, ast.While) for n in nodes)
    calls = {n.func.id if isinstance(n.func, ast.Name) else getattr(n.func, "attr", "")
             for n in nodes if isinstance(n, ast.Call)}
    return not_started, has_for, has_while, calls


def _timeout(signum, frame):
    raise TimeoutError()


def _problem(func, loop, banned, tests, hint):
    """Return None if the exercise passes, otherwise a list of lines to show."""
    name = func.__name__.split("_", 1)[1]
    for args, expected in tests:
        call = f"{name}({', '.join(repr(a) for a in args)})"
        signal.signal(signal.SIGALRM, _timeout)
        signal.alarm(2)
        try:
            got = func(*args)
        except TimeoutError:
            return [f"{call} never finished — your loop runs forever.",
                    "Does the number in your while condition change every turn?"]
        except Exception as err:
            return [f"{call} crashed: {type(err).__name__}: {err}", f"Hint: {hint}"]
        finally:
            signal.alarm(0)
        if got != expected:
            lines = [
                call, f"  should give: {expected!r}", f"  you gave:    {got!r}"]
            if got is None:
                lines.append("Did you forget  return  at the end?")
            lines.append(f"Hint: {hint}")
            return lines

    _, has_for, has_while, calls = _info(func)
    if loop == "for" and not has_for:
        return ["Right answer, but this one should use a FOR loop."]
    if loop == "while" and not has_while:
        return ["Right answer, but this one should use a WHILE loop."]
    if banned and banned in calls:
        return [f"Right answer, but try it without {banned}() — use the loop to count."]
    return None


def _run():
    done = 0
    for func, loop, banned, tests, hint in EXERCISES:
        label = f"{func.__name__.split('_')[0]}  {func.__name__.split('_', 1)[1]}"
        if _info(func)[0]:
            print(
                f"\n{BOLD}Next up: {label}{RESET}  — scroll to it and replace `pass`.")
            break
        problem = _problem(func, loop, banned, tests, hint)
        if problem:
            print(f"{RED}  ✗  {label}{RESET}")
            for line in problem:
                print(f"       {line}")
            break
        print(f"{GREEN}  ✓  {label}{RESET}")
        done += 1

    print(f"\n{BOLD}{done}/{len(EXERCISES)} done{RESET}")
    if done == len(EXERCISES):
        print("All done! Ready for for_while_practice.py.")


if __name__ == "__main__":
    _run()
