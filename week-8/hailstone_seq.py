def hailstone_seq(n=40):
    seq = [str(n)]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(str(n))
    print(", ".join(seq))