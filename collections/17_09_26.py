'''
a=[1,2,3]
b=a
b.append(4)#[1,2,3,4]
print(a)


c=a[:]
print(c)
c=a.copy()
c.append(9)
print(a)#[1,2,3,4]


import copy
grid=[[1,2],[3,4]]
shallow=grid.copy()
shallow[0][0]=99
print(grid)  #[[[99,2],[3,4]]]


deep=copy.deepcopy(grid)
print(grid)
print(deep)


def add(item, bucket=[]):
    bucket.append(item)
    return bucket
print(add(1))
print(add(2))   #[1,2]

def add(item,bucket=None):
    if bucket is None:
        bucket=[]
    bucket.append(item)
    return bucket
print(add(1))   #[1]
print(add(2))   #[2]



lst=list(map(int,input("Enter numbers into list:").split(',')))
b=lst.count(0)
for i in range(b):
    a=lst.pop(lst.index(0))
    lst.append(0)
print(lst)

'''

