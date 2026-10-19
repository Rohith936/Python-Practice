#1
'''
a=input()
a=list(a)
#print(len(set(a)))
if len(a)==len(set(a)):
    print("Unique")
else:
    print("Not Unique")
'''
#2
'''
a=input()
c=''
s=set(a)
for i in s:
    #print(a.count(i))
    c+=i+str(a.count(i))
print(c)
'''
#3
'''
a=input()
a=a.split(' ')
#print(a)
largest=a[0]
for i in a:
    #print(type(i))
    #print(type(largest))
    if len(largest)<len(i):
        largest=i
print(largest)
'''
#4
'''
a=input()
#print(a.title())
print(a.count(' '))
b=a.count(' ')
for i in a:
    while i==' ':
        i.upper()
        break
        
print(a)
'''
#5
a=int(input('Enter number of rows:'))
b=int(input('Enter number  of columns:'))
print('Enter elements into array:')
for i in range
