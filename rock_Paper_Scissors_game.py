import random

print("Welcome to Rock, Paper, Scissors Game!")

emoji = {'r': 'Rock 🪨', 'p': 'Paper 📄', 's': 'Scissors ✂️'}


def get_user_choice():
    while True:
        user_choice = input("rock, paper, or scissors (r,p,s): ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please choose 'r', 'p', or 's'.")


def display_choice(user_choice, computer_choice):
    print(f"You chose {emoji[user_choice]} \
        \nthe computer chose {emoji[computer_choice]}.")


def winner_determination(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):

        print("You win!")
    else:
        print("You lose!")


def play_game():

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(['r', 'p', 's'])
        display_choice(user_choice, computer_choice)
        winner_determination(user_choice, computer_choice)

        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()

            if play_again == 'y':
                print()
                break
            elif play_again == 'n':
                print("Thanks for playing! Goodbye.")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")


play_game()
