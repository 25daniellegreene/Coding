def findHypot(var1,var2):
    side3=((side1**2+side2**2)**0.5)
    return side3
side1=input('Enter the length of side 1:')
side1=float(side1)
side2=input('Enter the length of side2:')
side2=float(side2)
value=findHypot(side1,side2)
print(value)