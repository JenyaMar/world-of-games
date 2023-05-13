import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_input = None
    while user_input not in range(1, difficulty + 1):
        diff_choice = input(f'Please choose a whole number between 1 and {difficulty}: ')
        if diff_choice.isdigit():
            user_input = float(diff_choice)
    return user_input


def compare_results(user_num, secret_num):
    if user_num == secret_num:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty=difficulty)
    result = compare_results(user_num=user_guess, secret_num=secret_number)
    return result
