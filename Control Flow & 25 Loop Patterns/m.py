n=int(input())
a=n%10
c=0
while n>0:
    n//=10
    b=n%10
    c+=b
print(a+c)
