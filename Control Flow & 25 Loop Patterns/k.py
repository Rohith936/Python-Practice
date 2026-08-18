n=int(input())
if n<=0:
    print("Enter valid number")
else:
    res=0
    while n>0:
        res = res*10 + n%10
        n//=10
    print(res)
