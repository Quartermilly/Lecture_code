parking_time = float(input('How many hours have parked?? '))

# the max parking time is 2 hours

if parking_time >= 2:
    print('Warning! You should move your car. ')
    time_over = -2 + parking_time
    print('You are ' + str(time_over) + ' hours over.')
else:
    if parking_time <= 2:
        print('You still have time!')
        time_left = 2 - parking_time
        print('Time left is, ' + str(time_left) + ' Hours.')
print('This is the end of the program')
