player1 = input("Player 1, enter Rock, Paper, or Scissors: ")
player2 = input("Player 2, enter Rock, Paper, or Scissors: ")

valid = ["rock", "paper", "scissors"]

if player1 not in valid or player2 not in valid:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
elif player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
