result=1
a=int(input('a:'))
b=int(input('b:'))
while b>0:
    if b%2 != 0:
        result*=a
    a=a*a
    b//=2
print("Result:",result)
