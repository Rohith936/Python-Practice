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

'''
