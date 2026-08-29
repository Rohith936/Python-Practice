good = [[0]*3 for _ in range(3)]
good[1][2]=7
print(good)
bad=[[0]*3]*3
bad[0][1]=4
print(bad)
d=list(range(5,11))
print(d)
c=list('abc')
print(c)
f=[x*x for x in range(5)]
print(f)
b=[]
b.append(10)
b+=[40]
print(b)
lst=[10,20,30]
lst.append(40)
print(lst)
lst.insert(1,15)
print(lst)
lst.extend([50,60])
print(lst)
lst.append([70,80])
print(lst)
lst+=[90]
print(lst)
