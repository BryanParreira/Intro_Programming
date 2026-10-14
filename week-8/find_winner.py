def find_winner(player1="Rock", player2="Rock"):
    if player1 == player2:
        return "It's a tie!"
    if (player1 == "Rock" and player2 == "Scissors") or \
       (player1 == "Scissors" and player2 == "Paper") or \
       (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 wins!"
    return "Player 2 wins!"