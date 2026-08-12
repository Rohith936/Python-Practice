#1
x = 58329
a=x//10e3 #5
b=x//10e2
c=b%10 #8
d=x//10e1
e=d%10 #3
f=x//10
g=f%10 #2
h=x%10 #9
print(int(a+c+e+g+h))
