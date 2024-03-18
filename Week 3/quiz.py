answer = input('What is the state capital of Wisconsin? ' )  #it's madison

if answer.upper() == 'MADISON': # converts input to uppercase then checks against the uppercase MADISON
    print('Correct!')
else:
    print('The capital of Wisconsin is Madison.')

# you could write this code as
# if answer.upper() != 'MADISON':
    # print('the capital of wisconsin is madison.')
# else:
#   print('correct' )
