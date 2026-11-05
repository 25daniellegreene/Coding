odd=0
even=0
for x in range(4):
    num=input('Enter a number:')
    num=int(num)
    if num%2==0:
        even=(even+num)
    elif num%2==1:
        odd=(odd+num)
print('sum of even numbers:',even)
print('sum of odd numbers:',odd)