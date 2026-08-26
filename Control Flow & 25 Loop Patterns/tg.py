a=list(map(int,input().split(',')))
print(a)
total=0
maxi=a[0]
mini=a[0]
b=len(a)-1
for i in a:
    total+=i
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print(total)
print(maxi)
print(mini)
a=sorted(a)
print('min:',a[0])
print('max:',a[b])
