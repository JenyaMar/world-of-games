from Score import add_score
from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRouletteGame import play as play_currency_roulette


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\n' \
           f'Here you can find many cool games to play.'


def check_if_won(val, difficulty):
    if val:
        add_score(difficulty=difficulty)


def load_game():
    choice = 0
    choices = range(1, 4)
    print(
        """
        Please choose a game to play: 
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back 
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """
    )
    while choice not in choices:
        user_choice = input('Enter your choice, it should be a digit between 1 and 3: ')
        if user_choice.isdigit():
            choice = int(user_choice)

    difficulty = 0
    difficulty_levels = range(1, 6)
    while difficulty not in difficulty_levels:
        user_input = input('Please choose game difficulty from 1 to 5: ')
        if user_input.isdigit():
            difficulty = int(user_input)
    if choice == 1:
        won = play_memory(diff=difficulty)
    elif choice == 2:
        won = play_guess(difficulty=difficulty)
    else:
        won = play_currency_roulette(difficulty=difficulty)
    check_if_won(val=won, difficulty=difficulty)
