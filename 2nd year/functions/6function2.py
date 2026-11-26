def is_even(n):
    if n%2==0:
        return 'true'
    else:
        return 'false'
num=input('Enter an integer:')
num=int(num)
value=is_even(num)
print(value)
