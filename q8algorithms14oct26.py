sales=input('Enter your monthly sales:')
sales=float(sales)
if sales> 40000:
    commision= sales*0.15
else:
    commision= sales*0.05
print('Your commision is',commision)