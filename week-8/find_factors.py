def find_factors(num=36):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    return ", ".join(factors)