mood=input('How are you feeling:')
weather=input('What is the weather like:')
if mood=='happy':
    if weather=='sunny':
        print('Suggested playlist: Pop Hits')
    else:
         print('Suggested playlist: Top Charts')
elif mood=='sad':
    if weather=='rainy':
        print('Suggested playlist: Sad Acoustic')
    else:
         print('Suggested playlist: Top Charts')
elif mood=='relaxed':
    print('Suggested playlist: Chill Vibes')
else:
    print('Suggested playlist: Top Charts')
