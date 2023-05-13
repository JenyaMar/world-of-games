from Live import welcome, load_game

user_name = input('Hey, please enter your name: ')
print(welcome(user_name))
while True:
    user_input = 'yes'
    while user_input == 'yes':
        load_game()
        user_input = input('Do you want to play again? (yes): ').lower()
    if user_input != 'yes':
        break
