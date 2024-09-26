# ROCK, PAPER, SCISSORS GAME

import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)

def main():
    player = input("Rock, paper, scissors?: ").lower()

    if player not in choices:
        print("you wrote wrong")
        main()

    elif computer == player:
        print("Tie!")

    elif computer == "rock":
        if player == "paper":
            print("You won")
        elif player == "scissors":
            print("Computer won")

    elif computer == "paper":
        if player == "rock":
            print("Computer won")
        elif player == "scissors":
            print("You won")

    elif computer == "scissors":
        if player == "paper":
            print("Computer won")
        elif player == "rock":
            print("You won")

    print(f"computer made: {computer}")
    print("-------------------------")

    check_again = input("Do you wanna play again (Yes or no): ").lower()

    if check_again == "yes":
        main()
    elif check_again == "no":
        print("Good bye!")

main()
