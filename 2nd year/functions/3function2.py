def letter_func(var1,var2):
    newword=''
    for x in var1:
        if x!=var2:
            newword=(newword+x)
    return newword
word=input('Enter a word:')
letter=input('Enter a letter:')
value=letter_func(word,letter)
print(value)
