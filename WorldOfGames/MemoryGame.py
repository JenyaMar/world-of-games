import time
import random


def generate_sequence(difficulty):
    ran_nums = []
    for i in range(difficulty):
        ran_nums.append(random.randint(1, 101))
    return ran_nums


def get_list_from_the_user(difficulty):
    user_inputs = []
    for i in range(difficulty):
        user_input = input('Please enter a whole number: ')
        if user_input.isdigit():
            user_inputs.append(int(user_input))
        else:
            print('The input should be a whole number')
            user_inputs.append('')
            continue
    return user_inputs


def is_list_equal(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def play(diff):
    gen_seq = generate_sequence(difficulty=diff)
    print(f"{gen_seq} ", end="")
    time.sleep(1)
    print("\r", end="")
    user_list = get_list_from_the_user(difficulty=diff)
    result = is_list_equal(list1=gen_seq, list2=user_list)
    return result
