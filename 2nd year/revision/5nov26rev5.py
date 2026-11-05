a=input('Enter a number')
a=float(a)
b=input('Enter another number')
b=float(b)
if a!=b:
    if a%2==1:
        if b%2==1:
            print('a and b are different and are odd')
    elif a%2==0:
        elif b%2==0:
            print('a and b are different and are even')
else:
    print('Does not matter')
    
