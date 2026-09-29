"""
SOLUTIONS — only look after you've really tried!

There is almost always more than one right answer.
If yours passes check.py, it's correct, even if it looks different.
"""


# =====================================================================
# LEVEL 1 — for loops + range()
# =====================================================================

def ex1_count_up(n):
    result = []
    for number in range(1, n + 1):
        result.append(number)
    return result


def ex2_sum_to(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def ex3_evens_between(start, end):
    evens = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            evens.append(number)
    return evens


def ex4_times_table(n):
    lines = []
    for i in range(1, 11):
        lines.append(f"{n} x {i} = {n * i}")
    return lines


def ex5_factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


def ex6_fizzbuzz(n):
    result = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result


# =====================================================================
# LEVEL 2 — while loops
# =====================================================================

def ex7_countdown(n):
    result = []
    while n >= 0:
        result.append(n)
        n -= 1
    return result


def ex8_digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def ex9_count_digits(n):
    count = 1
    while n >= 10:
        n = n // 10
        count += 1
    return count


def ex10_first_power_over(base, limit):
    value = 1
    while value <= limit:
        value *= base
    return value


def ex11_collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def ex12_reverse_number(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result


# =====================================================================
# LEVEL 3 — strings
# =====================================================================

def ex13_count_vowels(s):
    count = 0
    for letter in s.lower():
        if letter in "aeiou":
            count += 1
    return count


def ex14_reverse_string(s):
    result = ""
    for letter in s:
        result = letter + result
    return result


def ex15_count_char(s, ch):
    count = 0
    for letter in s:
        if letter == ch:
            count += 1
    return count


def ex16_remove_spaces(s):
    result = ""
    for letter in s:
        if letter != " ":
            result += letter
    return result


def ex17_split_words(sentence):
    words = []
    word = ""
    for letter in sentence:
        if letter == " ":
            if word != "":
                words.append(word)
            word = ""
        else:
            word += letter
    if word != "":
        words.append(word)
    return words


def ex18_is_palindrome(s):
    cleaned = ""
    for letter in s.lower():
        if letter != " ":
            cleaned += letter
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def ex19_capitalize_words(s):
    result = ""
    new_word = True
    for letter in s:
        if new_word and letter != " ":
            result += letter.upper()
            new_word = False
        else:
            result += letter
        if letter == " ":
            new_word = True
    return result


def ex20_compress(s):
    if s == "":
        return ""
    result = ""
    current = s[0]
    count = 0
    for letter in s:
        if letter == current:
            count += 1
        else:
            result += current + str(count)
            current = letter
            count = 1
    result += current + str(count)
    return result


def ex21_longest_word(sentence):
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest


# =====================================================================
# LEVEL 4 — lists
# =====================================================================

def ex22_find_max(nums):
    biggest = nums[0]
    for number in nums:
        if number > biggest:
            biggest = number
    return biggest


def ex23_average(nums):
    if len(nums) == 0:
        return 0
    total = 0
    for number in nums:
        total += number
    return total / len(nums)


def ex24_only_positives(nums):
    result = []
    for number in nums:
        if number > 0:
            result.append(number)
    return result


def ex25_index_of(items, target):
    index = 0
    while index < len(items):
        if items[index] == target:
            return index
        index += 1
    return -1


def ex26_reverse_list(items):
    result = []
    index = len(items) - 1
    while index >= 0:
        result.append(items[index])
        index -= 1
    return result


def ex27_remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def ex28_running_total(nums):
    result = []
    total = 0
    for number in nums:
        total += number
        result.append(total)
    return result


def ex29_second_largest(nums):
    first = None
    second = None
    for number in nums:
        if first is None or number > first:
            second = first
            first = number
        elif number != first and (second is None or number > second):
            second = number
    return second


# =====================================================================
# LEVEL 5 — nested loops + putting it all together
# =====================================================================

def ex30_triangle(n):
    rows = []
    for row in range(1, n + 1):
        stars = ""
        for _ in range(row):
            stars += "*"
        rows.append(stars)
    return rows


def ex31_is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def ex32_primes_up_to(n):
    primes = []
    for number in range(2, n + 1):
        if ex31_is_prime(number):
            primes.append(number)
    return primes


def ex33_pairs_that_sum(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs


def ex34_flatten(list_of_lists):
    result = []
    for inner in list_of_lists:
        for item in inner:
            result.append(item)
    return result
