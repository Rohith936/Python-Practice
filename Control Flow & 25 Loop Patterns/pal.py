i=int(input())
count=len(str(i))
m=0
while count>0:
    m=i%10
    i//=10
    count-=1
print(count)
    
