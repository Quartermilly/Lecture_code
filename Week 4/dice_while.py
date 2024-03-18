import random
want_to_quit = ''

while not want_to_quit:
    dice_value = random.randint(1,6)
    print(f'You rolled a {dice_value}')
    want_to_quit = input('Roll again? press enter, any other key to quit.')


