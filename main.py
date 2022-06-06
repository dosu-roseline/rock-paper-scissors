
## let R = Rock
##     P = Paper
##     S = Scissors

import random

while True:
    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
    player = input("R, P, or S?:")


    if player == CPU:
        print('Player: ', player)
        print('CPU: ', CPU)
        print('Tie')
    elif player == 'R':
        if CPU == 'P':
            print('Player: ', player)
            print('CPU: ', CPU)
            print('You lose!')
        if CPU == 'S':
            print('Player: ', player)
            print('CPU: ', CPU)
            print('You win!')
    elif player == 'S':
        if CPU == 'R':
            print('Player: ', player)
            print('CPU: ', CPU)
            print('You lose!')
        if CPU == 'P':
            print('Player: ', player)
            print('CPU: ', CPU)
            print('You win!')
    elif player == 'P':
        if CPU == 'S':
            print('Player: ', (player))
            print('CPU: ', CPU)
            print('You lose!')
        if CPU == 'R':
            print('Player: ', player)
            print('CPU: ', CPU)
            print('You win!')
    else:
        print('Error: check your spelling')

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != 'yes':
        break
print('Bye!')