def odd_function(var1):
    count=0
    for x in range(var1):
        if x%2==0:
            count=(count+1)
    return count
num=input('Enter a number:')
num=int(num)
value=odd_function(num)
print(value)