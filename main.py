#! /usr/bin/python3

import sys
import combat_tracker
from unittest import main

health = 0
armor = 0
soak = 0

quit = False


try:
    health = int( sys.argv[1] )
    armor = int( sys.argv[2] )
    soak = int( sys.argv[3] )
except:
    print("Positive whole numbers required.\n")
    quit = True


player = combat_tracker.Tracker(health, armor, soak)

# Enter while loop, and keep it active while quit boolean is False.
while not quit:
    
    print(player)
    
    cmd = [x for x in input('$> ').split()]
    
    if cmd[0] == 'd':
        if len(cmd) < 2 or len(cmd) > 3:
            print('Did not enter the right amount of arguments.\n')
            continue
        
        if cmd[1].isdigit() == False:
            print('You need to enter whole numbers.\n')
            continue
        
        if len(cmd) == 2:
            player.damage(int(cmd[1]))
        
        else:
            if cmd[2].isdigit() == False:
                print('You need to enter whole numbers.\n')
                continue
            player.damage(int(cmd[1]), int(cmd[2]))
    
    
    elif cmd[0] == 'h':
        if len(cmd) < 2 or len(cmd) > 2 or cmd[1].isdigit() == False:
            print('You need to enter a whole number.\n')
            continue
        
        player.heal(int(cmd[1]))
    
    
    elif cmd[0] == 'help':
        print('Commands\n\n')
        print(' d {damage} {soak_damage}\n    : Calculates damage to health, armor, and soak. Do not need to enter soak damage if it is equal to damage.\n\n')
        print(' h {amount}\n    : Increases health by the amount passed as an argument.\n\n')
        print(' help\n    : Shows a list of the commands.\n\n')
        print(' quit\n    : Ends the program.\n\n')
        print(' reset\n    : Resets stats to max values.\n\n')
        print(' set {health} {armor} {soak}\n    : Sets current stat values to the arguments given\n\n')
        print(' setmax {health} {armor} {soak}\n    : Sets max stat values to the arguments given\n\n')
    
    
    elif cmd[0] == 'reset':
        player.reset_stats()
    
    
    elif cmd[0] == 'set':
        if len(cmd) < 4 or len(cmd) > 4:
            print('Not enough arguments\n')
            continue
        
        if cmd[1].isdigit() == False or cmd[2].isdigit() == False or cmd[3].isdigit() == False:
            print('You need to enter a whole number.\n')
            continue
        
        player.set_current_stats(int(cmd[1]), int(cmd[2]), int(cmd[3]))
    
    
    elif cmd[0] == 'setmax':
        if len(cmd) < 4 or len(cmd) > 4:
            print('Invalid arguments\n')
            continue
        
        if cmd[1].isdigit() == False or cmd[2].isdigit() == False or cmd[3].isdigit() == False:
            print('You need to enter a whole number.\n')
            continue
        
        player.set_max_stats(int(cmd[1]), int(cmd[2]), int(cmd[3]))
    
    
    elif cmd[0] == 'quit':
        break
    
    
    else:
        if len(cmd[0]) > 10:
            print('{0:<10.10}... is not a recognized command.\n'.format(cmd[0]))
        else:
            print('{0:<10} is not a recognized command.\n'.format(cmd[0]))

# Run the tests automatically.
#main(module='test_module', exit=False)



