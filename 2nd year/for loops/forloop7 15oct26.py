name=input('Enter your name:')
num=input('Enter a number:')
num=int(num)
if num<10:
    for x in range(num):
        print(name)
else:
    print('Number is too high')
