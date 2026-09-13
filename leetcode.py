'''
l1=[1,2,3]
l2=[3,4,5]
a=int(''.join(map(str,l1)))#123 -> means joining the list items and converting into integer 
b=int(''.join(map(str,l2)))
result=str(a+b)
print(list(map(int,result)))#converting lists




c=[1,2,3]
result=''.join(map(str,c))#123 -> means joining the list items
print(result)
print(type(result))



def nu(num):
    a=0
    while num:
        if num%2==0:
            num/=2
        else:
            num-=1
        a+=1
    return a
print(nu(17))




nums=[12,324,1234]
a=len(nums)-1
d=0
while a>=0:
    c=nums[a]
    b=0
    while c:
        c//=10
        b+=1
    a-=1
    if b%2==0:
        d+=1
print(d)



n=234
n=list(str(n))
a=len(n)-1
b=1
c=0
while a>=0:
    b*=int(n[a])
    c+=int(n[a])
    a-=1
print(b-c)





candies = [2,3,5,1,3]
extraCandies=3
a=len(candies)
b=[]
for i in range(a):
    c=candies[i]+extraCandies
    b.append(c)
d=min(b)
for i in range(a):
    if b[i]==d:
        b[i]=False
    else:
        b[i]=True
print(b)
    
'''  
    
    
    
        
        


