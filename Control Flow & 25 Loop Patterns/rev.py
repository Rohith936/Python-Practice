s=input('s:')
a=''
n=list(input('List:').split(','))
b=''
for i in s:
    a=i+a
print(a)
for j in  n:
    b=j+' '+b
print(b.split(' '))





f = list(input("List: ").split(','))

o = len(f)

for i in range(o // 2):
    f[i], f[o - 1 - i] = f[o - 1 - i], f[i]

print("Reversed list:", a)

    
       


