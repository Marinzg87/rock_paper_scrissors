from asciiArt import scissors as scissors
from asciiArt import rock as rock
from asciiArt import paper as paper
import random

welcome_message = """
This is classic rock paper scissors game
1. Rock wins against scissors.
2. Scissors wins against paper.
3. Paper wins against rock.
"""

bets = [scissors, rock, paper]

print(welcome_message)
user_bet = int(input("Choose one: 1 - Rock, 2 - Paper, 3 - Scissors: "))
computer_bet = random.randint(1, 3)

if user_bet == computer_bet:
    print("Draw!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 1 and computer_bet == 3:
    print("You win!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 1 and computer_bet == 2:
    print("You lost!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 2 and computer_bet == 1:
    print("You win!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 2 and computer_bet == 3:
    print("You lost!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 3 and computer_bet == 2:
    print("You win!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
elif user_bet == 3 and computer_bet == 1:
    print("You lost!")
    print(f"Your bet: {bets[user_bet - 1]}")
    print("#######################")
    print(f"Computer bet: {bets[computer_bet - 1]}")
