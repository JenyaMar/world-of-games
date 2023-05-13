import random

from currency_converter import CurrencyConverter

curr_conv = CurrencyConverter()


def get_money_interval(difficulty):
    conv_rate = curr_conv.convert(1, 'USD', 'ILS')
    rand_num = random.randint(1, 100)
    total = rand_num * conv_rate
    inter = (total - (5 - difficulty), total + (5 - difficulty))
    result = get_guess_from_user(rand_num=rand_num, interval=inter)
    return result


def get_guess_from_user(rand_num, interval):
    user_input = ''
    while not isinstance(user_input, float):
        try:
            user_input = float(input(f'Guess how much ILS is {rand_num}$: '))
        except ValueError:
            print('Please enter a valid number.')
    low, high = interval
    if low <= user_input <= high:
        return True
    return False


def play(difficulty):
    get_money_interval(difficulty=difficulty)
