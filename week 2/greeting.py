name = input('please enter your name: ')
print('Hello, ' + name)
letters = len(name)  # len function is calculating the length of a string
print(letters)  # i'd like to remove this, its redundant
print('Your name has ' + str(letters) + ' letters')