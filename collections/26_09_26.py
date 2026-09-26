#1
'''
from collections import Counter
def anagram(words):
    a=[]
    b=len(words)-1
    for i in words:
        a.append(i)
        while b:
            if Counter(i)==Counter(words[b]):
                a.append(words[b])
                del words[b]
            b-=1
    return a
words = list(("eat", "tea", "tan", "ate", "nat", "bat"))
print(anagram(words))
'''
#2
'''
a=list(map(int,input().split(',')))
print(set(a))
'''
#3
'''
a=list(map(int,input().split(',')))
b=[]
for i in range(max(a)):
    if i not in a:
        b.append(i)
print(b)
'''
#3
'''
a=list(map(int,input('a:').split(',')))
b=list(map(int,input('b:').split(',')))
print(set(a)&set(b))
'''
#5
'''
a=input('s:')
b=set(a)
if len(a)==len(b):
    print(True)
else:
    print(False)
'''         
