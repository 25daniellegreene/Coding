def num_function(var1):
    count=0
    for x in num:
        count=(count+1)
    return(count)
num=input('Enter a number:')
value=num_function(num)
print(value)