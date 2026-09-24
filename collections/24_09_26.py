#1
'''
t=(10,20,30,40,50)
print(t[1])
print(t[3])
print(t[-1])
'''
#2
'''
t = ("apple", "banana", "cherry", "mango")
c=0
for i in t:
    c+=1
print(f"length:{c}")
'''
#3
'''
t = (10, 20, 30, 40, 50)
if 30 in t:
    print('there')
'''
#4
'''
t = (1, 2, 3, 2, 4, 2, 5)
count=0
for i in t:
    if i==2:
        count+=1
print(f"no.of 2's:{count}")
'''
#5,6,7,8,9
'''
t = (10, 20, 30, 40, 50, 60)
print(t[1:4])
t1=(1, 2, 3, 4, 5)
print(t1[::-1])
t1=list(t1)
print(type(t1),t1)
'''
#10
'''
t = (45, 12, 78, 23, 9, 56)
print(f"min:{min(t)},max:{max(t)}")
'''
