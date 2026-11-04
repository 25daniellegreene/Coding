secret=7
guess=input('Guess a number from 1-10:')
guess=int(guess)
if guess == secret:
    print('Bingo! Correct answer')
elif guess == secret+1:
    print('Close enough to the correct answer')
else:
    print('not close enough')
    