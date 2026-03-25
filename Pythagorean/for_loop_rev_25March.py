# a=input('Enter an integer value:')
# a=int(a)
# b=input('Enter another integer value:')
# b=int(b)
# c=input('Enter another integer value:')
# c=int(c)
a_range=input('Enter another a number for your range:')
a_range=int(a_range)
b_range=input('Enter another a number for your range:')
b_range=int(b_range)
c_range=input('Enter another a number for your range:')
c_range=int(c_range)
for a in range (1,21):
    for b in range (1,21):
        for c in range (1,21):
            a_squ=(a*a)
            b_squ=(b*b)
            c_squ=(c*c)
            if (a_squ)+(b_squ)== c_squ:
                print('You have entered a pythagorean triple')
