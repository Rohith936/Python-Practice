a=int(input("a:"))
b=int(input("b:"))
while b:
    a,b=b,a%b
print(a)
