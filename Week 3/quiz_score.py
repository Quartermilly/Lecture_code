quiz_score = float(input('Enter score for quiz, out of 100: '))
if quiz_score == 90:
    print('Your letter grade is an A')
elif quiz_score >= 80:
    print('Your letter grade is a B')
elif quiz_score >= 70:
    print('Your letter grade is a C')
elif quiz_score >= 60:
    print('Your letter grade is a D')
else:
    print('Sorry, you have failed the quiz.')
