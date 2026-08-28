a=list(map(int,input().split(',')))
b=a[0]
d=0
for i in a:
    if i>b:
        d=i
        a.remove(d)
        if i>b:
            b=i
print(b)


a = list(map(int, input().split(',')))

largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second:
        second = i

print(second)
