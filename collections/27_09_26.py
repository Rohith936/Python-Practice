#6
'''
a=list(map(int,input('a:').split(',')))
b=list(map(int,input('b:').split(',')))
c=set(a)
d=set(b)
if len(a)==len(c) and len(b)==len(d):
    print(list(c&d))
else:
    e=[x for x in zip(a,b)]
    print(e)
'''
#7
'''
a = list(map(int, input('a: ').split(',')))
s = set(a)
for i in range(1,len(a) + 1):
    if i not in s:
        print(i)
        break
'''
#8
'''
words = ["bella","label","roller"]
g=len(words)-1
a=len(words)-1
word=words[0]
b=[]
while a:
    for i in word:
        if i in words[a]:
            b.append(i)
    b.append('|')
    a-=1
print(b)
f=set()
for i in b:
    if b.count(i)>=g:
        f.add(i)
print(f)
'''
