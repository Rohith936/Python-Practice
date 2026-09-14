lst=['a','b','c','d','e']
a=len(lst)-1
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[2])
print('z' in lst)
lst.index('c')
lst.count('e')


x=123
x=str(x)
x=list(x)
y=len(x)-1
print(x.index(x[y])+1)#count digits
