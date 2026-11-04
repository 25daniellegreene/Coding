num1=input('Enter a number:')
num1=int(num1)
num2=input('Enter another number:')
num2=int(num2)
num3=input('Enter another number:')
num3=int(num3)
if num1+num2==num3:
    print('sum of first and second number equal third number')
elif num3+num2==num1:
    print('sum of third and second number equal first number')
elif num1+num3==num2:
    print('sum of first and third number equal second number')