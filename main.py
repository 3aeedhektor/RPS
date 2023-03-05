import random
from config import  GAME_CHOICES, RULES, scoreboard

#get and validate player input, recursively
def get_user_choice():
    user_input = input('Enter your choice please (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print("Oops!!, wrong choice, try again please...")
        return get_user_choice()
    else:
        return user_input

#choice random from GAME_CHOICES
def get_system_choice():
    system_choice = random.choice(GAME_CHOICES)
    return system_choice

def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None

    else:
        return RULES[tuple(sorted(match))]

def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'You win'
    else:
        scoreboard['system'] += 1
        msg = 'You lose'

    print("#" * 30)
    print("##", f"User: {scoreboard['user']}".ljust(24), '##')
    print('##', f"System: {scoreboard['system']}".ljust(24), '##')
    print('##', f"Result: {msg}".ljust(24), '##')
    print('#' * 30)


#Main play ground handler

def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if user_choice == winner:
            msg = "You Winner"
            result['user'] += 1
        elif system_choice == winner:
            msg = "You lose"
            result['system'] += 1
        else:
            msg = "Draw"
        print(f"User: {user_choice}\t system: {system_choice}\t Result: {msg}")

    update_scoreboard(result)

    #play again
    play_again = input("Do you want play again (y/n): ")
    if play_again == 'y':
        play()

if __name__ == '__main__':
    play()