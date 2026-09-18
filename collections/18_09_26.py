'''
a=list(map(int,input("Enter numbers into list:").split(',')))
if len(a)<2:
    print(bool(0))
else:
    b=sorted(set(a))
    print("Second largest:",b[-2])


def second_largest(nums):
    first = second = float('-inf')
    for x in nums:
        if x > first:
            second, first = first, x
        elif first > x > second:
            second = x
    return None if second == float('-inf') else second
print(second_largest([10, 5, 10, 8, 3]))

a=list(map(int,input("Enter numb ers into list:").split(',')))
k=int(input('k:'))
b=len(a)-1
for i in range(k):
    c=a.pop()
    a.insert(0,c)
print(a)


a=list(map(int,input("a:").split(',')))
b=list(map(int,input("b:").split(',')))
a=sorted(set(a))
b=sorted(set(b))
print(sorted(set(a+b)))

'''
#TUPLES
'''
t=(1,2,3)
t2=1,2,3    #parentheses are optional!
empty=()
single=(5,)  #the comma makes its a tuple
print(type(single))
not_a_tuple=(5)
print(type(not_a_tuple)) #int
form_tier=tuple([1,2,3])
print(form_tier)
from_str=tuple("abc")
print(from_str)

point=3,4
x,y=point

a,b=1,2
a,b=b,a

first,*middle,last=[1,2,3,4,5,6]
print(first,middle,last)

_,score=("Asha",95)
print(score)

pairs=[('a',1),('b',2)]
for name,num in pairs:
    print(name,num)

#supports slicing,in,+,*,len
t=(10,20,30,20,50)
t[1]  #20
t[1:4]  #(20,30,20)
print(t+(50,)) #concat
print(t*2)                  
print(20 in t)
print(t.count(20))
print(t.index(30))
t=t[:2]+(99,)+t[3:]
print(t)

grid={}
grid[(0,0)]='start'
grid[(2,3)]='goal'
print(grid[(0,0)])
bad=(1,[2,3])
print(grid)
seen=set()
seen.add((3,2))
seen.add(5)
print(seen)
print(type(seen))
print(type(grid))
print((3,4) in seen) #false

from collections import namedtuple
Student=namedtuple("Student",['name','score','branch'])
s=Student('Asha',92,'CSE')
print(s.name)
print(s.score)
print(s[2])
print(s._asdict())
s2=s._replace(score=95)
print(s)

def status(nums):
    return min(nums),max(nums),sum(nums)/len(nums)
mi,ma,avg=status([10,3,2,65,3,67,3,23])
print(mi,ma,avg)

records=[('Ravi',88,21),('Asha',92,20),('Kiran',88,19),('Sam',92,22)]
records.sort(key=lambda r:(-r[1],r[2],r[0]))
print(records)
for i in records:
    print(i)

def uniqe_items(points):
    return len(set(points))
pts=[(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
print(uniqe_items(pts))

'''
#SETS
'''
s={1,2,3}
s2=set([1,2,3,2])
print(s2)
empty=set()  #set
not_a_set={}  #dictionary

s={1,2,3}
s.add(4)
s.add(2)
s.update([5,6])
print(s)
s.remove(6)
print(s)
s.discard(99)  #removes if present but dont throw a error
print(s)
x=s.pop()
print(s)
s.clear()
print(s)
'''
