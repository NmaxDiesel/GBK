import random

def get_user_choice():
    choice = input("Pilih gunting, batu, atau kertas: ")
    return choice.lower()

def get_computer_choice():
    choices = ["gunting", "batu", "kertas"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Seri"
    elif (user_choice == "gunting" and computer_choice == "kertas") or \
         (user_choice == "batu" and computer_choice == "gunting") or \
         (user_choice == "kertas" and computer_choice == "batu"):
        return "Anda menang!"
    else:
        return "Komputer menang!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("Anda memilih:", user_choice)
    print("Komputer memilih:", computer_choice)

    winner = determine_winner(user_choice, computer_choice)
    print(winner)

play_game()
