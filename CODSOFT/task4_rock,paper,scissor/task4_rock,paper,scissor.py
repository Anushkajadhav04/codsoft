import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)
    print(get_winner(user_choice, computer_choice))

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break