import random
import time
import os


user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

draw = {
    "rock": r'''
   _____                         ____
---'      )__                 __(     '---
      (_ /___)               (___\ _)    
      (_____)                 (_____) 
      (____)                   (____) 
---._(___)                      (___)_.--- 
''',
    "paper": r'''
    _______                    _______
---'   ____)____          ____(____   '---
       ) _______)        (________ (
      /  ________)      (_________  \
         _______)        (______
---.__________)            (__________.---
''',
    "scissors": r'''
    _______                    _______
---'   ____)____          ____(____   '---
       ) _______)        (________ (
      /  ________)      (_________  \
        (____)              (____)
---.____(___)                (___)__.---
'''
}

#rock : paper
#rock : scissors
#paper : rock
#paper : scissors
#scissors : rock
#scissors : paper
combinations = {
    "rock_paper": r'''
    _____                      _______
---'      )__             ____(____   '---
      (_ /___)           (________ (
      (_____)           (_________  \
      (____)             (______
---._(___)                 (__________.---
''',
    "rock_scissors": r'''
    _____                       _______
---'      )__              ____(____   '---
      (_ /___)            (________ (
      (_____)            (_________  \
      (____)                 (____)
---._(___)                    (___)__.---
''',
    "paper_rock": r'''
    _______                      ____
---'   ____)____              __(     '---
       ) _______)            (___\ _)    
      /  ________)            (_____) 
         _______)              (____) 
---.__________)                 (___)_.---
''',
    "paper_scissors": r'''
    _______                     _______
---'   ____)____           ____(____   '---
       ) _______)         (________ (
      /  ________)       (_________  \
         _______)            (____)
---.__________)               (___)__.---
''',
    "scissors_paper": r'''
    _______                    _______
---'   ____)____          ____(____   '---
       ) _______)        (_______  (
      /  ________)      (________   \
        (____)           (_______
---.____(___)               (_________.---
''',
   "scissors_rock": r'''
    _______                      ____
---'   ____)____              __(     '---
       ) _______)            (___\ _)    
      /  ________)            (_____) 
        (____)                 (____) 
---.____(___)                   (___)_.---
'''
}

hands_ready = r'''

 _____  ______          _______     _____  
 |  __ \|  ____|   /\   |  __ \ \   / /__ \ 
 | |__) | |__     /  \  | |  | \ \_/ /   ) |
 |  _  /|  __|   / /\ \ | |  | |\   /   / / 
 | | \ \| |____ / ____ \| |__| | | |   |_|  
 |_|  \_\______/_/    \_\_____/  |_|   (_)
    _____                         ____
---'      )__                 __(     '---
      (_ /___)               (___\ _)    
      (_____)                 (_____) 
      (____)                   (____) 
---._(___)                      (___)_.--- 
'''

counter = {
"three": r'''
                     #####
                        ##
                      ###
                       ##
                   #####
''',
"two": r'''
                    #####
                       ##
                     ##
                   ##
                   ######
''',
"one": r'''
                      ##
                     ###
                      ##
                      ##
                     ####
''',
"go": r'''
                #####      ######
               ##         ##   ##
              ##  ####   ##   ##
             ##    #    ##   ##
             ######     ######
'''
}



def get_ready():
    #clear screen
    os.system("cls" if os.name == "nt" else "clear")
    
    #prepare for the fight
    print(hands_ready)
    time.sleep(0.5)

    #3, 2, 1, Go
    for keys, count in counter.items():
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print(count)
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


#main
while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    #exist if q
    if user_input == 'q':   break
    
    #retry if not a valid value
    if user_input not in options:
        continue

    get_ready()

    #computer turn
    #random: 0 ==> rock, 1 ==> paper, scissors ==> 2
    computer_pick = options[random.randint(0, 2)]
    print(f'Computer picked {computer_pick.upper()}.')

    #if draw
    if user_input == computer_pick:
        print(draw[user_input])
        print('               It\'s a draw!\n')
    
    elif user_input == 'rock':
        print(combinations[user_input+'_'+computer_pick])
        if computer_pick == 'paper':
            print('               Computer wins!\n')
            computer_wins += 1
        if computer_pick == 'scissors':
            print('               You win!\n')
            user_wins += 1

    elif user_input == 'paper':
        print(combinations[user_input+'_'+computer_pick])
        if computer_pick == 'scissors':
            print('               Computer wins!\n')
            computer_wins += 1
        if computer_pick == 'rock':
            print('               You win!\n')
            user_wins += 1

    elif user_input == 'scissors':
        print(combinations[user_input+'_'+computer_pick])
        if computer_pick == 'rock':
            print('               Computer wins!\n')
            computer_wins += 1
        if computer_pick == 'paper':
            print('               You win!\n')
            user_wins += 1

    #stats
    print(f'You: {user_wins}\t\t\t\tComputer: {computer_wins}')

print('Goodbye!')
quit()
