#1

a=input()
b=list(a)
x=0
y=len(b)-1
while x<y:
    b[x],b[y]=b[y],b[x]
    x+=1
    y-=1
#print(''.join(a))
b=''.join(b)
if a==b:
    print(f'{a} is a Palindrome')
else:
    print(f'{a} is not a palidrome')

#2

word1=input()
word2=input()
a=list(word1)
b=list(word2)
c=0
for word in a[:]:
    print(word)
    if word not in b:
        a.remove(word)
        c+=1
for word in a[:]:
    e=a.count(word) 
    f=b.count(word)
    if e>f:
        a.remove(word)
        c+=1
#print(a,b)
while a != b:
    for word in b:
        if word in a:
            c=a.index(word) 
            d=b.index(word)
            if c != d:
                a.remove(word)
                a.insert(d,word)
                #print(a)
                c+=1
        else:
            h=b.index(word)
            a.insert(h,word)
            c+=1
        if a==b:
            break
print(a,b,c)

#virtual environment
'''
#A virtual environment in python is an isolated environment on your computer, where you can run and test your python projects
#Has is own python interpreter
#Has its own set of installed packages
#Can have different versions of the same package
# VI is important becz:
#It prevents package version confilcts between packages
#Makes projects more portable and reproductive
#Keeps your system python iinstallation is clear
#Allows testing with different python versions
'''
