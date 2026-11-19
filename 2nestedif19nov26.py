income=input('Enter your monthly income:')
income=float(income)
age=input('Enter your age')
age=int(age)
habit=input('What are your spending habits like:')
if income<2000:
    if 20<=age<=40:
        if habit=='high':
            print('Basic savings plan. Monthly savings target: €417')
elif 2000<income<5000:
    if habit=='moderate':
        print('Standard savings plan. Monthly savings target:€',income/5)
elif income>=5000:
    if 30>age:
        if habit=='low':
            print('Aggresive Investment plan. Projected savings: €',(income/10)*5)
else:
    print('The app offers a Flexible Budget plan with general tips to improve savings')
