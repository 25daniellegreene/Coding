ppl=input('How many people would you like to invite:')
ppl=int(ppl)
if ppl<10:
    for x in range(ppl):
        name=input('Enter their name:')
        print(name,'has been invited')
elif ppl>=10:
    print('Too many people')
