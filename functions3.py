def some_variable(var1,var2):
    div=var1/var2
    return div
num1=input('Enter a number:')
num1=float(num1)
num2=input('Enter another number:')
num2=float(num2)
value=some_variable(num1,num2)
print(value)