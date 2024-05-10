import random

choices = ["rock", "paper", "scissors"]

while True:
    player = None

    computer = random.choice(choices)

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("computer:", computer)
    print("player:", player)

    if player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose")
        else:
            print("You win")
    elif player == "paper":
        if computer == "scissors":
            print("You lose")
        else:
            print("You win")
    elif player == "scissors":
        if computer == "rock":
            print("You lose")
        else:
            print("You win")

    play_again = input("play again (yes/no): ").lower()
    if play_again != "yes":
          break        

print("game over")