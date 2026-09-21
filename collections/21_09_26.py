'''
s=input('s:')
t=input('t:')

a=dict(zip(list(s),list(t)))
print(a)

b=dict(zip(list(t),list(s)))
print(b)

if len(a)==len(b):
    print(True)
    
d={'a':1,'b':2,'c':3}

for k in d:
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,'->',v)

print(list(d.keys()))
print(sum(d.values()))
print(max(d,key=d.get))

squares={x:x*x for x in range(5)}
print(squares)

from_two = {k: v for k, v in zip("abc", [1, 2, 3])}
print(from_two)

a=[10,3,8,20,5]
print(max(a)-min(a))

b=[1,2,3,5,6]
for i in range(1,len(b)+1):
    if i not in b:
        print(i)

c=[1,3,4,2,3,1]
j=set()
for i in c:
    if c.count(i)>1:
        j.add(i)
print(j)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c=set(a)
d=set(b)
print(c.intersection(d))
e=[]
for i in a:
    if i in b:
        e.append(i)
print(e)
print(sorted(a+b))
'''
