
import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Stone-Paper-Scissor Game!")
user_choice = input("Enter your choice (stone/paper/scissor): ").lower()
computer_choice = get_computer_choice()

print(f"Computer chose: {computer_choice}")
print(get_winner(user_choice, computer_choice))
