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
#1
'''
a=int(input('a:'))
b=int(input('b:'))
a,b=b,a
print(f"a:{a},b:{b}")
'''
#2
'''
a=int(input('a:'))
if a>0:
    print(f"{a} is positive")
elif a<0:
    print(f"{a} is negative")
else:
    print("ZERO")
'''
#3
'''
print('Hello World')
'''
#4
'''
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
x=max(a,b,c)
print(f"largest:{x}")
'''
#5
'''
a=int(input('a:'))
print('Even') if a%2==0 else print('Odd')
'''
#5,6
'''
a=input()
b=int(input())
print(f"reverse:{a[::-1]}")
b=str(b)
b=int(b[::-1])
print(f"reverse:{b}")
'''
#7
'''
a=int(input())
a=list(str(a))
c=0
for i in a:
    i=int(i)
    c+=i
print(f"sum:{c}")
'''
#8
'''
a=input()
if a[::-1]==a:
    print(f"{a} is palindrome")
else:
    print("Not a palindrome")
'''
#9
'''
a=input()
b=len(a)
c=0
for i in a:
    if i in "aeiouAEIOU":
        c+=1
print(f"no of vowels:{c}")
print(f"no of consonants:{b-c}")
'''
#10
'''
from collections import Counter
a=input('s:')
c=Counter(a)
print(f'frequency:{c}')
'''
#11
'''
a=input('a:')
a=a.split(' ')
print(f"No of words:{len(a)}")
'''
#12
'''
a=[x*3 for x in range(5)]
print(a)
'''
#13
'''
a=input()
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
'''
#14
'''
x={'a':1,'b':2}
y={'c':2,'d':3,'a':4}
print(x|y)
'''
#15
'''
a=list(map(int,input('a:').split(',')))
print(set(a))
'''
#16
'''
b=list(map(int,input('b:').split(',')))
a=max(b)
c=[]
for i in range(1,a+1):
    if i not in b:
        c.append(i)
print(c)
'''
#17
'''
a=list(map(int,input('a:').split(',')))
b=list(map(int,input('b:').split(',')))
print(f"common elements:{set(a)&set(b)}")
'''
#18
'''
a=input()
a=a.split(' ')
b=[len(x) for x in a ]
c=max(b)
for i in a:
    if len(i)==c:
        print(f'longest word is {i}')
'''
#19
'''
a=list(map(int,input('a:').split(',')))
maxi=a[0]
mini=a[0]
for i in range(0,len(a)):
    if maxi<a[i]:
        maxi=a[i]
    elif mini>a[i]:
        mini=a[i]
print(f"max:{maxi},min:{mini}")
'''
#20
'''
a=list(map(str,input('a:').split(',')))
b=len(a)-1
for i in range(len(a)//2):
    a[i],a[b]=a[b],a[i]
    b-=1
print(a)
'''
#21
'''
a=list(map(int,input('a:').split(',')))
b=max(a)
a.remove(b)
print(f"second largest:{max(a)}")
'''
#22
'''
a=list(map(str,input('a:').split(',')))
print(list(set(a)))
'''
#23
'''
from collections import Counter
a=input()
c=Counter(a)
b=c.values()
d=Counter(b)
k=max(d.keys())
print(c.most_common(k))
'''
#24
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input('n:'))
print(fact(n))
'''
#25
'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input('n:'))
print(fib(n))
'''
#26
'''
a=input()
for i in a:
    if a.count(i)==1:
        print(i)
        break
    else:
        print('all characters are repeated')
'''
