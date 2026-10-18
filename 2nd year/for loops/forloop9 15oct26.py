direction=input('Would you like to count up or down:')
if direction == 'up':
    topnum=input('Enter a number to count to:')
    topnum=int(topnum)
    for x in range(1,topnum+1):
        print(x)
elif direction == 'down':
    countdown=input('Enter a number below 20:')
    countdown=int(countdown)
    for x in range(20,countdown,-1):
        print(x)
else:
    print('I do not understand')
