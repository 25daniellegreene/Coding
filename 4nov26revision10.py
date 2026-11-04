day=input('pick either the weather,day or date:')
if day == 'weather':
    mood=input('Enter sunny or rainy:')
elif day == 'day':
    mood=input('Enter a day (Monday-Sunday):')
elif day == 'date':
    mood=input('Enter the date:')
    mood=int(mood)
if mood == 'sunny'or'Saturday'or'Sunday' or mood%2==0:
    print('It is a happy day')
elif mood == 'rainy'or'Monday'or'Tuesday'or'Wednesday'or'Thursday'or'Friday' or mood%2==1:
    print('It is a sad day')