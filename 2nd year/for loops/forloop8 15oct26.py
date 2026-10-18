total=0
for i in range(5):
    num1=input('Enter a number:')
    num1=int(num1)
    enter1=input('Would you like this number to be added to the total:')
    if enter1 == 'yes':
        total=total+num1
print(total,'is the total')
