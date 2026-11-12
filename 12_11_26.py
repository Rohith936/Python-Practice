'''
a={'a':3,'b':2}
b={'b':2,'a':3}
print(a==b)

x=input()
c={}
d={}
for i in x:
    if i in c:
        c[i]+=1
        d[i]+=1
    else:
        c[i]=1
        d[i]=1

for i in c:
    print(i)
    if i not in 'balon':
        del d[i]
print(d)

a=''
for i in c:
    if i in 'balon':
        a+=i
'''
s=input()
b=s.count('b')
a=s.count('a')
l=s.count('l')//2
o=s.count('o')//2
n=s.count('n')
print(b,a,l,o,n)
print(min(b,a,l,o,n))
