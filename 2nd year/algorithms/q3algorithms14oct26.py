num=input('Enter a number:')
num2=input('Enter a second number:')
num3=input('Enter a third number:')
num3=int(num3)
num=int(num)
num2=int(num2)
if num>num2:
    if num>num3:
        print(num,'is the biggest number')
if num2>num:
    if num2>num3:
        print(num2,'is the biggest number')
if num3>num:
    if num3>num2:
        print(num3,'is the biggest number')
