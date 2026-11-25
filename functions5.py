def some_function(var1):
    total=0
    for letter in var1:
        total=total+1
    return total
word=input('Enter a word:')
var2= some_function(word)
print(var2)