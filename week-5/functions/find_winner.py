def find_winner(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


player1 = input("Player 1, choose Rock, Paper, or Scissors: ")
player2 = input("Player 2, choose Rock, Paper, or Scissors: ")
print(find_winner(player1, player2))
