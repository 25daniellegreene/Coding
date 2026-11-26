def num_test(var1):
    if var1>10:
        return'Greater than 10'
    elif var1==10:
        return'Equal to 10'
    else:
        return'Less than 10'
num=input('Enter a number:')
num=float(num)
value=num_test(num)
print(value)
