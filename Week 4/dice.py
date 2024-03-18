import random

number_of_dice = int(input('How many dice to roll? '))

#  print('about to roll ' + str(number_of_dice) + ' dice')
print(f'about to roll {number_of_dice} dice.')  # (f)ormat string
for dice in range(number_of_dice):  # rolls 5 dice
    dice_value = random.randint(1, 6)
    # print('Dice ' + str(dice) + ' value is ' + str(dice_value))
    print(f'Dice {dice+1} value is {dice_value}')  # I like this method much better
