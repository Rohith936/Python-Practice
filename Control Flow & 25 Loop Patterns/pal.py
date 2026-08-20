i=int(input())
a=i
count=len(str(i))
rev=0
while count>0:
    m=i%10
    rev=rev*10+m
    i//=10
    count-=1
if a==rev:
    print("palindrome")
else:
    print("Not a palindrome")
    
    
