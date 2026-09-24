def total_score(aces, winning_shots):
    return aces * 2 + winning_shots * 1


aces = int(input("Enter the number of aces: "))
winning_shots = int(input("Enter the number of winning shots: "))
print(total_score(aces, winning_shots))
